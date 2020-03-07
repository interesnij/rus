from django.views.generic.base import TemplateView
from main.models import Item
from communities.models import Community, CommunityMembership
from follows.models import CommunityFollow
from common.checkers import check_can_get_posts_for_community_with_name
from django.views.generic import ListView
from rest_framework.exceptions import PermissionDenied
from common.utils import is_mobile


class ItemsCommunity(ListView):
	template_name = None
	paginate_by = 30

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_template_list(folder="c_lenta/", template="list.html", request=request)
		try:
			self.fixed = Item.objects.get(community=community, is_fixed=True)
		except:
			self.fixed = None
		return super(ItemsCommunity,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(ItemsCommunity,self).get_context_data(**kwargs)
		context['object'] = self.fixed
		context["community"] = self.community
		return context

	def get_queryset(self):
		item_list = self.community.get_posts().order_by('-created')
		return item_list


class ItemCommunity(TemplateView):
    model = Item
    template_name = None

    def get(self,request,*args,**kwargs):
        self.community = Community.objects.get(pk=self.kwargs["pk"])
        self.item = Item.objects.get(uuid=self.kwargs["uuid"])
        self.items = self.community.get_posts()
        self.next = self.items.filter(pk__gt=self.item.pk).order_by('pk').first()
        self.prev = self.items.filter(pk__lt=self.item.pk).order_by('-pk').first()
        self.template_name = self.community.get_template_list(folder="c_lenta/", template="item.html", request=request)
        return super(ItemCommunity,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super(ItemCommunity,self).get_context_data(**kwargs)
        context["object"] = self.item
        context["community"] = self.community
        context["next"] = self.next
        context["prev"] = self.prev
        return context


class CommunityDetail(TemplateView):
    template_name = None
    membersheeps = None
    common_friends = None

    def get(self,request,*args,**kwargs):
        self.community = Community.objects.get(pk=self.kwargs["pk"])
        self.membersheeps=self.community.get_community_with_name_members(self.community.name)[0:6]
        try:
            self.common_friends = request.user.get_common_friends_of_community(self.community.pk)[0:6]
        except:
            self.common_friends = None
        self.template_name = self.community.get_template(folder="c_detail/", template="community.html", request=request)
        return super(CommunityDetail,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(CommunityDetail,self).get_context_data(**kwargs)
        context["membersheeps"]=self.membersheeps
        context["community"]=self.community
        context["common_friends"]=self.common_friends
        return context


class CommunityDetailReload(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.community = Community.objects.get(pk=self.kwargs["pk"])
        self.membersheeps=self.community.get_community_with_name_members(self.community.name)[0:6]
        try:
            self.common_friends = request.user.get_common_friends_of_community(self.community.pk)[0:6]
        except:
            self.common_friends = None
        self.template_name = self.community.get_template(folder="c_detail/", template="community.html", request=request)
        return super(CommunityDetailReload,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(CommunityDetailReload,self).get_context_data(**kwargs)
        context["membersheeps"]=self.membersheeps
        context["community"]=self.community
        context["common_friends"]=self.common_friends
        return context
