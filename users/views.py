from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from generic.mixins import CategoryListMixin
from profiles.models import UserProfile
from datetime import datetime, timedelta
from users.models import User
from posts.models import Post
from posts.forms import PostHardForm, PostLiteForm, PostMediumForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator



class AllUsers(TemplateView,CategoryListMixin):
	template_name="all_users.html"


class ProfileUserView(LoginRequiredMixin, ListView):
	template_name = 'user.html'
	form = PostMediumForm
	model=Post

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])

		self.posts=Post.objects.filter(creator=self.user)
		paginator = Paginator(self.posts, 10)
		return super(ProfileUserView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(ProfileUserView, self).get_context_data(**kwargs)
		context['user'] = self.user
		context['posts'] = self.posts
		context['form'] = self.form

		return context
