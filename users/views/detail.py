from django.views.generic.base import TemplateView
from users.models import User
from common.checkers import check_is_not_blocked_with_user_with_id, check_is_connected_with_user_with_id
from django.shortcuts import render_to_response
from common.utils import is_mobile


class UserItemView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from main.models import Item
        self.user = User.objects.get(pk=self.kwargs["pk"])
        self.item = Item.objects.get(uuid=self.kwargs["uuid"])
        self.item.views += 1
        self.item.save()

        self.items = self.user.get_posts()
        self.template_name = self.user.get_template_list_user(folder="lenta/", template="item.html", request=request)
        self.next = self.items.filter(pk__gt=self.item.pk).order_by('pk').first()
        self.prev = self.items.filter(pk__lt=self.item.pk).order_by('-pk').first()
        return super(UserItemView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(UserItemView,self).get_context_data(**kwargs)
        context["object"] = self.item
        context["user"] = self.user
        context["next"] = self.next
        context["prev"] = self.prev
        context["request_user"]=self.request.user
        return context


class AllPossibleUsers(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from common.utils import is_mobile

		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		if is_mobile(request):
			self.template_name = "mob_possible_list.html"
		else:
			self.template_name = "possible_list.html"
        return super(AllPossibleUsers,self).get(request,*args,**kwargs)


class UserCommunities(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        from communities.models import Community

        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.popular_list = Community.get_trending_communities()[0:7]
        if self.user == request.user:
            if self.user.get_staffed_communities():
                self.template_name = "user_community/my_communities_with_staffed.html"
            else:
                self.template_name = "user_community/my_communities.html"
        elif request.user != self.user and request.user.is_authenticated:
            if request.user.is_blocked_with_user_with_id(user_id=self.user.id):
                self.template_name = "user_community/block_communities.html"
            elif self.user.is_closed_profile():
                if not request.user.is_connected_with_user_with_id(user_id=self.user.id):
                    self.template_name = "user_community/close_communities.html"
                else:
                    self.template_name = "user_community/communities.html"
            else:
                self.template_name = "user_community/communities.html"

        elif request.user.is_anonymous and self.user.is_closed_profile():
            self.template_name = "user_community/close_communities.html"

        elif request.user.is_anonymous and not self.user.is_closed_profile():
            self.template_name = "user_community/anon_communities.html"
        return super(UserCommunities,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserCommunities, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['popular_list'] = self.popular_list
        return context

class UserMusic(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_template_user(folder="user_music/", template="music.html", request=request)
        return super(UserMusic,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserMusic, self).get_context_data(**kwargs)
        context['user'] = self.user
        return context


class ProfileUserView(TemplateView):
    template_name = None

    def get(self,request,*args,**kwargs):
        self.user=User.objects.get(pk=self.kwargs["pk"])
        self.template_name = self.user.get_template_user(folder="account/", template="user.html", request=request)
        return super(ProfileUserView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        from communities.models import Community

        context = super(ProfileUserView, self).get_context_data(**kwargs)
        context['user'] = self.user
        context['communities'] = Community.get_trending_communities()[0:5]
        if self.request.user.is_authenticated:
            context['common_frends'] = self.user.get_common_friends_of_user(self.request.user)[0:5]
        return context
