from django.views.generic.base import TemplateView
from communities.models import Community
from stst.models import CommunityNumbers


class CommunityCoberturaMonth(TemplateView):
	template_name = None

	def get(self,request,*args,**kwargs):
		self.community = Community.objects.get(pk=self.kwargs["pk"])
		self.template_name = self.community.get_manage_template(folder="community_stat/", template="cobertura_month.html", request=request)
		self._months = [i.month for i in CommunityNumbers.objects.values_list('created', flat=True).distinct('user')]
		self.months = self._months
		self.month_query = CommunityNumbers.objects.filter(community=self.community.pk, created__month=self.months[0]).distinct().values('platform')
		self.phone_count = self.month_query.filter(platform=1)
		self.comp_count = self.month_query.filter(platform=0)
		self.phone = len(self.phone_count)/len(self.month_query)*100
		self.comp = len(self.comp_count)/len(self.month_query)*100
		return super(CommunityCoberturaMonth,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context = super(CommunityCoberturaMonth,self).get_context_data(**kwargs)
		context["community"] = self.community
		context["phone"] = self.phone or 0
		context["comp"] = self.comp or 0
		context["months"] = self.months or None
		context["current"] = self.months[0] or None
		context["month_views"] = len(self.month_query) or None
		return context
