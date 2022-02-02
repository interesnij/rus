from django.views import View
from users.models import User
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from planner.models import *
from managers.forms import ModeratedForm
from django.views.generic.base import TemplateView
from managers.models import Moderated
from common.templates import get_detect_platform_template, get_staff_template
from logs.model.manage_planner import PlannerManageLog


class WorkspaceCloseCreate(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.workspace = Workspace.objects.get(pk=self.kwargs["pk"])
        if request.user.is_moderator():
            self.template_name = get_staff_template("managers/manage_create/planner/workspace_close.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(WorkspaceCloseCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(WorkspaceCloseCreate,self).get_context_data(**kwargs)
        context["object"] = self.workspace
        return context

    def post(self,request,*args,**kwargs):
        workspace, form = Workspace.objects.get(pk=self.kwargs["pk"]), ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid() and request.user.is_moderator():
            mod = form.save(commit=False)
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=workspace.pk, type=38)
            moderate_obj.create_close(object=workspace, description=mod.description, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=workspace.pk, manager=request.user.pk, action_type=PlannerManageLog.WORKSPACE_CLOSED)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class WorkspaceCloseDelete(View):
    def get(self,request,*args,**kwargs):
        workspace = Workspace.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=workspace.pk, type=38)
            moderate_obj.delete_close(object=workspace, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=workspace.pk, manager=request.user.pk, action_type=PlannerManageLog.WORKSPACE_CLOSED_HIDE)
            return HttpResponse()
        else:
            raise Http404


class WorkspaceRejectedCreate(View):
    def get(self,request,*args,**kwargs):
        workspace = Workspace.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=workspace.pk, type=38)
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=workspace.pk, manager=request.user.pk, action_type=PlannerManageLog.WORKSPACE_REJECT)
            return HttpResponse()
        else:
            raise Http404

class WorkspaceUnverify(View):
    def get(self,request,*args,**kwargs):
        workspace = Workspace.objects.get(pk=self.kwargs["pk"])
        obj = Moderated.get_or_create_moderated_object(object_id=workspace.pk, type=38)
        if request.is_ajax() and request.user.is_moderator():
            obj.unverify_moderation(workspace, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=obj.object_id, manager=request.user.pk, action_type=PlannerManageLog.WORKSPACE_UNVERIFY)
            return HttpResponse()
        else:
            raise Http404


class BoardPlannerCloseCreate(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.board = Board.objects.get(pk=self.kwargs["pk"])
        if request.user.is_moderator():
            self.template_name = get_staff_template("managers/manage_create/planner/board_close.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(BoardPlannerCloseCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(BoardPlannerCloseCreate,self).get_context_data(**kwargs)
        context["object"] = self.board
        return context

    def post(self,request,*args,**kwargs):
        board, form = Board.objects.get(pk=self.kwargs["pk"]), ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid() and request.user.is_moderator():
            mod = form.save(commit=False)
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=board.pk, type=39)
            moderate_obj.create_close(object=board, description=mod.description, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=board.pk, manager=request.user.pk, action_type=PlannerManageLog.BOARD_CLOSED)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class BoardPlannerCloseDelete(View):
    def get(self,request,*args,**kwargs):
        board = Board.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=board.pk, type=39)
            moderate_obj.delete_close(object=board, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=board.pk, manager=request.user.pk, action_type=PlannerManageLog.BOARD_CLOSED_HIDE)
            return HttpResponse()
        else:
            raise Http404

class BoardPlannerRejectedCreate(View):
    def get(self,request,*args,**kwargs):
        board = Board.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=board.pk, type=39)
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=board.pk, manager=request.user.pk, action_type=PlannerManageLog.BOARD_REJECT)
            return HttpResponse()
        else:
            raise Http404

class BoardPlannerUnverify(View):
    def get(self,request,*args,**kwargs):
        board = Board.objects.get(pk=self.kwargs["pk"])
        obj = Moderated.get_or_create_moderated_object(object_id=board.pk, type=39)
        if request.is_ajax() and request.user.is_moderator():
            obj.unverify_moderation(board, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=obj.object_id, manager=request.user.pk, action_type=PlannerManageLog.BOARD_UNVERIFY)
            return HttpResponse()
        else:
            raise Http404


class ColumnPlannerCloseCreate(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.column = Column.objects.get(pk=self.kwargs["pk"])
        if request.user.is_moderator():
            self.template_name = get_staff_template("managers/manage_create/planner/column_close.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(ColumnPlannerCloseCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(ColumnPlannerCloseCreate,self).get_context_data(**kwargs)
        context["object"] = self.column
        return context

    def post(self,request,*args,**kwargs):
        column, form = Column.objects.get(pk=self.kwargs["pk"]), ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid() and request.user.is_moderator():
            mod = form.save(commit=False)
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=column.pk, type=40)
            moderate_obj.create_close(object=column, description=mod.description, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.COLUMN_CLOSED)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class ColumnPlannerCloseDelete(View):
    def get(self,request,*args,**kwargs):
        column = Column.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=column.pk, type=40)
            moderate_obj.delete_close(object=column, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.COLUMN_CLOSED_HIDE)
            return HttpResponse()
        else:
            raise Http404


class ColumnPlannerRejectedCreate(View):
    def get(self,request,*args,**kwargs):
        column = Column.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=column.pk, type=40)
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.COLUMN_REJECT)
            return HttpResponse()
        else:
            raise Http404

class ColumnPlannerUnverify(View):
    def get(self,request,*args,**kwargs):
        column = Column.objects.get(pk=self.kwargs["pk"])
        obj = Moderated.get_or_create_moderated_object(object_id=column.pk, type=40)
        if request.is_ajax() and request.user.is_moderator():
            obj.unverify_moderation(column, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=obj.object_id, manager=request.user.pk, action_type=PlannerManageLog.COLUMN_UNVERIFY)
            return HttpResponse()
        else:
            raise Http404


class CardPlannerCloseCreate(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.column = ColumnCard.objects.get(pk=self.kwargs["pk"])
        if request.user.is_moderator():
            self.template_name = get_staff_template("managers/manage_create/planner/column_close.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(CardPlannerCloseCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CardPlannerCloseCreate,self).get_context_data(**kwargs)
        context["object"] = self.column
        return context

    def post(self,request,*args,**kwargs):
        column, form = ColumnCard.objects.get(pk=self.kwargs["pk"]), ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid() and request.user.is_moderator():
            mod = form.save(commit=False)
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=column.pk, type=41)
            moderate_obj.create_close(object=column, description=mod.description, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.CARD_CLOSED)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CardPlannerCloseDelete(View):
    def get(self,request,*args,**kwargs):
        column = ColumnCard.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=column.pk, type=41)
            moderate_obj.delete_close(object=column, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.CARD_CLOSED_HIDE)
            return HttpResponse()
        else:
            raise Http404


class CardPlannerRejectedCreate(View):
    def get(self,request,*args,**kwargs):
        column = ColumnCard.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=column.pk, type=41)
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=column.pk, manager=request.user.pk, action_type=PlannerManageLog.CARD_REJECT)
            return HttpResponse()
        else:
            raise Http404

class CardPlannerUnverify(View):
    def get(self,request,*args,**kwargs):
        column = ColumnCard.objects.get(pk=self.kwargs["pk"])
        obj = Moderated.get_or_create_moderated_object(object_id=column.pk, type=41)
        if request.is_ajax() and request.user.is_moderator():
            obj.unverify_moderation(column, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=obj.object_id, manager=request.user.pk, action_type=PlannerManageLog.CARD_UNVERIFY)
            return HttpResponse()
        else:
            raise Http404


class CommentPlannerCloseCreate(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.comment = ColumnCardComment.objects.get(pk=self.kwargs["pk"])
        if request.user.is_moderator():
            self.template_name = get_staff_template("managers/manage_create/planner/comment_close.html", request.user, request.META['HTTP_USER_AGENT'])
        else:
            raise Http404
        return super(CommentPlannerCloseCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(CommentPlannerCloseCreate,self).get_context_data(**kwargs)
        context["object"] = self.comment
        return context

    def post(self,request,*args,**kwargs):
        comment, form = ColumnCardComment.objects.get(pk=self.kwargs["pk"]), ModeratedForm(request.POST)
        if request.is_ajax() and form.is_valid() and request.user.is_moderator():
            mod = form.save(commit=False)
            moderate_obj = Moderated.get_or_create_moderated_object(object_id=comment.pk, type=42)
            moderate_obj.create_close(object=comment, description=mod.description, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=comment.pk, manager=request.user.pk, action_type=PlannerManageLog.COMMENT_CLOSED)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CommentPlannerCloseDelete(View):
    def get(self,request,*args,**kwargs):
        comment = ColumnCard.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=comment.pk, type=42)
            moderate_obj.delete_close(object=comment, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=comment.pk, manager=request.user.pk, action_type=PlannerManageLog.COMMENT_CLOSED_HIDE)
            return HttpResponse()
        else:
            raise Http404


class CommentPlannerRejectedCreate(View):
    def get(self,request,*args,**kwargs):
        comment = ColumnCardComment.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax() and request.user.is_moderator():
            moderate_obj = Moderated.objects.get(object_id=comment.pk, type=42)
            moderate_obj.reject_moderation(manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=comment.pk, manager=request.user.pk, action_type=PlannerManageLog.COMMENT_REJECT)
            return HttpResponse()
        else:
            raise Http404

class CommentPlannerUnverify(View):
    def get(self,request,*args,**kwargs):
        comment = ColumnCardComment.objects.get(pk=self.kwargs["pk"])
        obj = Moderated.get_or_create_moderated_object(object_id=comment.pk, type=42)
        if request.is_ajax() and request.user.is_moderator():
            obj.unverify_moderation(comment, manager_id=request.user.pk)
            PlannerManageLog.objects.create(item=obj.object_id, manager=request.user.pk, action_type=PlannerManageLog.COMMENT_UNVERIFY)
            return HttpResponse()
        else:
            raise Http404
