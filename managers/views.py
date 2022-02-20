from django.views.generic.base import TemplateView
from common.templates import get_detect_platform_template
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.views import View
from users.models import User


class ManagersView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_manager() or request.user.is_superuser:
            self.template_name = get_detect_platform_template("managers/managers.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(ManagersView,self).get(request,*args,**kwargs)

class SuperManagersView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_supermanager() or request.user.is_superuser:
            self.template_name = get_detect_platform_template("managers/managers.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(SuperManagersView,self).get(request,*args,**kwargs)


class SendManagerMessages(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        if request.user.is_administrator():
            self.template_name = get_detect_platform_template("managers/manage_create/message/send_messages.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(SendManagerMessages,self).get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        from chat.forms import MessageForm

        form = MessageForm(request.POST, request.FILES)

        if request.is_ajax() and form.is_valid() and request.user.is_administrator():
            from chat.models import Message

            form_post = form.save(commit=False)
            Message.get_or_create_manager_chat_and_send_message(
                creator_pk = request.user.pk,
                text = form_post.text,
                voice = request.POST.get('voice'),
                attach = request.POST.getlist('attach_items')
            )
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class SanctionItemCreate(TemplateView):
    template_name, open_suspend, open_warning_banner, is_admin = None, None, None, None

    def get(self,request,*args,**kwargs):
        from common.utils import get_item_of_type, get_comment, get_list_of_type

        self._type = request.GET.get('type')
        self._subtype = request.GET.get('subtype')

        if self._subtype and self._subtype == "comment":
            self.item = get_comment(self._type)
        elif self._subtype and self._subtype == "planner":
            self.item = get_planner(self._type)
        elif self._type[0] == "l":
            self.item = get_list_of_type(self._type)
            self.open_suspend = True
        elif "use" in self._type:
            from users.models import User
            self.item = User.objects.get(pk=self._type[3:])
            self.open_suspend, self.open_warning_banner, self.is_admin = True, True, True
        elif "com" in self._type:
            from communities.models import Community
            self.item = Community.objects.get(pk=self._type[3:])
            self.open_suspend, self.open_warning_banner, self.is_admin = True, True, True
        else:
            self.item = get_item_of_type(self._type)

        if (self.is_admin and request.user.is_administrator()) or request.user.is_moderator():
            self.template_name = get_detect_platform_template("managers/sanction.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(SanctionItemCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(SanctionItemCreate,self).get_context_data(**kwargs)
        context["object"] = self.item
        context["type"] = self._type
        context["subtype"] = self._subtype
        context["open_suspend"] = self.open_suspend
        context["open_warning_banner"] = self.open_warning_banner
        return context

    def post(self, request, *args, **kwargs):
        from django.http import HttpResponse, HttpResponseBadRequest
        from managers.models import Moderated, ModeratedLogs
        from common.utils import get_item_for_post_sanction
        from managers.forms import ModeratedForm

        type = request.POST.get('_type')
        subtype = request.POST.get('_subtype')

        list = get_item_for_post_sanction(type, subtype)
        if (list[2] and request.user.is_administrator()) or not request.user.is_moderator():
            return HttpResponseBadRequest()

        form = ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid():
            mod = form.save(commit=False)
            case = request.POST.get('case')
            item = list[0]
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=item.pk, type=list[1])
            if case == "close":
                moderate_obj.create_close(object=item, description=mod.description, manager_id=request.user.pk)
                ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=list[3][0])
                item.close_item()

            elif case == "suspend":
                from django.utils import timezone
                from common.tasks import custom
                from datetime import datetime, timedelta

                moderate_obj.status = Moderated.SUSPEND
                moderate_obj.description = mod.description
                moderate_obj.save()
                number = request.POST.get('number')
                if number == '4':
                    duration_of_penalty = timezone.now() + timezone.timedelta(days=30)
                elif number == '3':
                    duration_of_penalty = timezone.now() + timezone.timedelta(days=7)
                elif number == '2':
                    duration_of_penalty = timezone.now() + timezone.timedelta(days=3)
                elif number == '1':
                    duration_of_penalty = timezone.now() + timezone.timedelta(hours=6)

                moderate_obj.create_suspend(manager_id=request.user.pk, duration_of_penalty=duration_of_penalty)
                ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=list[3][1])

        		custom.apply_async((item), eta=duration_of_penalty)
            elif case == "warning_banner":
                moderate_obj.status = Moderated.BANNER_GET
                moderate_obj.description = mod.description
                moderate_obj.save()
                moderate_obj.create_warning_banner(manager_id=request.user.pk)
                ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=31)
                item.banner_item()
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class SanctionItemDelete(View):
    def get(self, request, *args, **kwargs):
        from django.http import HttpResponse, HttpResponseBadRequest
        from managers.models import Moderated, ModeratedLogs
        from common.utils import get_item_for_post_sanction

        type = request.GET.get('_type')
        subtype = request.GET.get('_subtype')

        list = get_item_for_post_sanction(type, subtype)
        if (list[2] and request.user.is_administrator()) or not request.user.is_moderator():
            return HttpResponseBadRequest()

        if request.is_ajax():
            item = list[0]
            moderate_obj = Moderated.objects.get(object_id=item.pk, type=list[1])
            if item.type[:4] == "_CLO":
                moderate_obj.delete_close(object=item, manager_id=request.user.pk)
                ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=list[3][2])
                item.abort_close_item()

            elif item.type[:4] == "_SUS":
                moderate_obj.delete_suspend(manager_id=request.user.pk)
                item.unsuspend_item()

                if item.type[0] == "l":
                    log_number = 10
                else:
                    log_number = 11
                ModeratedLogs.objects.create(type=type, object_id=item.pk, manager=request.user.pk, action=log_number)

            elif item.type[:4] == "_BAN":
                moderate_obj.delete_warning_banner(manager_id=request.user.pk)
                ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=log_number)
                item.unbanner_item()
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class RejectedItemClaims(View):
    def get(self, request, *args, **kwargs):
        from django.http import HttpResponse, HttpResponseBadRequest
        from managers.models import Moderated, ModeratedLogs
        from common.utils import get_item_for_post_sanction

        type = request.GET.get('_type')
        subtype = request.GET.get('_subtype')

        list = get_item_for_post_sanction(type, subtype)
        if (list[2] and request.user.is_administrator()) or not request.user.is_moderator():
            return HttpResponseBadRequest()

        if request.is_ajax():
            item = list[0]
            moderate_obj = Moderated.objects.get(object_id=item.pk, type=list[1])
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=list[3][3])
            return HttpResponse()
        else:
            return HttpResponseBadRequest()


class UnverifyItemCreate(View):
    def get(self, request, *args, **kwargs):
        from django.http import HttpResponse, HttpResponseBadRequest
        from managers.models import Moderated, ModeratedLogs
        from common.utils import get_item_for_post_sanction

        type = request.GET.get('_type')
        subtype = request.GET.get('_subtype')

        list = get_item_for_post_sanction(type, subtype)
        if (list[2] and request.user.is_administrator()) or not request.user.is_moderator():
            return HttpResponseBadRequest()

        if request.is_ajax():
            item = list[0]
            moderate_obj = Moderated.objects.get(object_id=item.pk, type=list[1])
            moderate_obj.unverify_moderation(item, manager_id=request.user.pk)
            ModeratedLogs.objects.create(type=list[1], object_id=item.pk, manager=request.user.pk, action=list[3][4])
            return HttpResponse()
        else:
            return HttpResponseBadRequest()
