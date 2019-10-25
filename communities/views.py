from django.views.generic import ListView
from users.models import User
from communities.models import Community
from django.views.generic.detail import DetailView



class CommunitiesView(ListView):
	template_name="communities.html"
	model=Community

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		self.groups=Community.objects.filter(starrers=self.user)
		return super(CommunitiesView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(CommunitiesView,self).get_context_data(**kwargs)
		context["groups"]=self.groups
		context['user'] = self.user
		return context

class CommunityDetailView(DetailView):
	template_name="community_detail.html"
	model=Community


class AllCommunities(ListView):
    template_name="all_communities.html"
    model=User
