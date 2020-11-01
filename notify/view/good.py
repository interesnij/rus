from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from notify.model.good import GoodNotify, GoodCommunityNotify
from common.template.user import get_settings_template


class GoodNotificationListView(LoginRequiredMixin, ListView):
    model = GoodNotify
    context_object_name = 'notification_list'
    template_name = None

    def get(self,request,*args,**kwargs):
        self.template_name = get_settings_template("notify/good/user_notify_list.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(GoodNotificationListView,self).get(request,*args,**kwargs)

    def get_queryset(self, **kwargs):
        notify = GoodNotify.objects.filter(recipient=self.request.user)
        return notify


class GoodCommunityNotificationListView(LoginRequiredMixin, ListView):
    model = GoodCommunityNotify
    context_object_name = 'notification_list'
    template_name = None

    def get(self,request,*args,**kwargs):
        self.template_name = get_settings_template("notify/good/community_notify_list.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(GoodCommunityNotify,self).get(request,*args,**kwargs)

    def get_queryset(self, **kwargs):
        notify = GoodCommunityNotify.objects.filter(community__creator=self.request.user)
        return notify


@login_required
def good_user_all_read(request):
    request.user.good_notifications.mark_all_as_read()
    _next = request.GET.get('next')
    if _next:
        return redirect(_next)
    return redirect('good_user_all_read')

@login_required
def good_community_all_read(request):
    request.user.good_community_notifications.mark_all_as_read()
    _next = request.GET.get('next')
    if _next:
        return redirect(_next)
    return redirect('good_community_all_read')


class GoodLastNotify(ListView):
    template_name = None
    paginate_by = 15

    def get(self,request,*args,**kwargs):
        self.template_name = get_settings_template("notify/good/most_recent.html", request.user, request.META['HTTP_USER_AGENT'])
        return super(GoodLastNotify,self).get(request,*args,**kwargs)

    def get_queryset(self):
        notifications = self.request.user.good_notifications.get_most_recent()
        return notifications
