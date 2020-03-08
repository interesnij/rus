import json, requests
from django.views.generic.base import TemplateView
from users.model.profile import *
from common.utils import get_client_ip
from users.models import User

class StatView(TemplateView):
    template_name="stat.html"

    def get(self,request,*args,**kwargs):
        self.ip = get_client_ip(request)
        self.user = User.objects.get(pk=self.kwargs["pk"])
        try:
            self.olds_ip = IPUser.objects.get(user=self.user)
        except:
            self.olds_ip = IPUser.objects.create(user=self.user)

        if not self.olds_ip.ip_1:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.js = self.response.json()
            self.sity = json.dumps(self.response["city"])
            self.region = json.dumps(self.response["region"])
            self.country = json.dumps(self.response["country"])
            try:
                self.loc = OneUserLocation.objects.get(user=self.user)
            except:
                self.loc = OneUserLocation.objects.create(user=self.user)
            self.loc.sity_ru = self.sity.get('sity_ru', None)
            self.loc.sity_en = self.sity.get('sity_en', None)
            self.loc.region_ru = self.region.get('region_ru', None)
            self.loc.region_en = self.region.get('region_en', None)
            self.loc.country_ru = self.country.get('country_ru', None)
            self.loc.country_en = self.country.get('country_en', None)
            self.loc.save()
        elif not self.olds_ip.ip_2 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = TwoUserLocation.objects.get(user=self.user)
            except:
                self.loc = TwoUserLocation.objects.create(user=self.user)
            self.loc.sity_ru = self.data.sity.name_ru
            self.loc.sity_en = self.data.sity.name_en
            self.loc.region_ru = self.data.region.name_ru
            self.loc.region_en = self.data.region.name_en
            self.loc.country_ru = self.data.sity.country_ru
            self.loc.country_en = self.data.sity.country_en
            self.loc.save()
        elif not self.olds_ip.ip_3 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = ThreeUserLocation.objects.get(user=self.user)
            except:
                self.loc = ThreeUserLocation.objects.create(user=self.user)
            self.loc.sity_ru = self.data.sity.name_ru
            self.loc.sity_en = self.data.sity.name_en
            self.loc.region_ru = self.data.region.name_ru
            self.loc.region_en = self.data.region.name_en
            self.loc.country_ru = self.data.sity.country_ru
            self.loc.country_en = self.data.sity.country_en
            self.loc.save()
        elif self.olds_ip.ip_3 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = ThreeUserLocation.objects.get(user=self.user)
            except:
                self.loc = ThreeUserLocation.objects.create(user=self.user)
            self.loc.ip_1 = self.ip
            self.loc.ip_2 = None
            self.loc.ip_3 = None
            self.loc.sity_ru = self.data.sity.name_ru
            self.loc.sity_en = self.data.sity.name_en
            self.loc.region_ru = self.data.region.name_ru
            self.loc.region_en = self.data.region.name_en
            self.loc.country_ru = self.data.sity.country_ru
            self.loc.country_en = self.data.sity.country_en
            self.loc.save()
        else:
            pass

        return super(StatView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(StatView,self).get_context_data(**kwargs)
        context["ip"]=self.ip
        context["data"]=self.loc
        return context
