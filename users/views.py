from django.views.generic.base import TemplateView
from users.models import User, UserProfile
from posts.models import Post
from connections.models import Connection
from communities.models import Community
from posts.forms import PostHardForm, PostLiteForm, PostMediumForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,HttpResponse,Http404
from users.forms import GeneralUserForm, AboutUserForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView


class AllUsers(ListView):
	template_name="all_users.html"
	model = User
	paginate_by = 15

	def get_queryset(self, **kwargs):
		users=User.objects.all()
		return users



class ProfileUserView(TemplateView):
	template_name = 'user.html'
	form = PostMediumForm

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		self.frends=Connection.objects.filter(target_connection__user=self.user)
		self.frends2=Connection.objects.filter(target_connection__target_user=self.user)
		self.communities=Community.objects.filter(starrers=self.user)
		self.posts=Post.objects.filter(creator=self.user)
		return super(ProfileUserView,self).get(request,*args,**kwargs)

	def get_context_data(self, **kwargs):
		context = super(ProfileUserView, self).get_context_data(**kwargs)
		context['user'] = self.user
		context['posts'] = self.posts
		context['frends'] = self.frends
		context['frends2'] = self.frends2
		context['form_medium'] = self.form
		context['communities'] = self.communities
		return context


class UserGeneralChange(LoginRequiredMixin, UpdateView):
	template_name = "user_general_form.html"
	form_class = GeneralUserForm
	success_url = "/"

	def get_queryset(self):
		try:
			queryset = User.objects.filter(id=self.request.user.id)
		except:
			queryset = User.objects.filter(id=self.request.user.id)
		return queryset

	def form_valid(self, form, **kwargs):
		super(UserGeneralChange, self).form_valid(form)
		profile = form.save(commit=False)
		user = self.request.user
		user.first_name = form.cleaned_data['first_name']
		user.last_name = form.cleaned_data['last_name']
		user.save()
		profile.sity = form.cleaned_data['sity']
		profile.phone = form.cleaned_data['phone']
		profile.vk_url = form.cleaned_data['vk_url']
		profile.youtube_url = form.cleaned_data['youtube_url']
		profile.facebook_url = form.cleaned_data['facebook_url']
		profile.instagram_url = form.cleaned_data['instagram_url']
		profile.twitter_url = form.cleaned_data['twitter_url']
		#profile.avatar = form.cleaned_data['avatar']
		profile.save()
		return HttpResponseRedirect(self.get_success_url())

class UserAboutChange(TemplateView):
	template_name = "user_about_form.html"
	form=None
	profile=None

	def get(self,request,*args,**kwargs):
		self.profile=UserProfile.objects.get(pk=self.kwargs["pk"])
		self.form=AboutUserForm(instance=self.profile)
		return super(UserAboutChange,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(UserAboutChange,self).get_context_data(**kwargs)

		context["profile"]=self.profile
		context["form"]=self.form
		return context

	def post(self,request,*args,**kwargs):
		self.profile=UserProfile.objects.get(pk=self.kwargs["pk"])
		self.form=Blog2Form(request.POST,instance=self.profile)
		if self.form.is_valid():
			self.form.save()
			if request.is_ajax():
				return HttpResponse ('!')
		return super(UserAboutChange,self).post(request,*args,**kwargs)



class PostUserView(ListView):
	template_name = 'post_list.html'
	model = Post
	paginate_by = 10

	def get_queryset(self, **kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		return Post.objects.filter(creator=self.user)

class UserDesign(TemplateView):
	template_name="user_design.html"
