import json, requests
from django.views.generic.base import TemplateView
from users.model.profile import *
from common.utils import get_client_ip
from common.location import data
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
            self.data = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            #self.data = data
            try:
                self.loc = OneUserLocation.objects.get(user=self.user)
            except:
                self.loc = OneUserLocation.objects.create(user=self.user)
            self.sity = self.data['city']
            self.region = self.data['region']
            self.country = self.data['country']
            self.loc.city_ru = self.sity['name_ru']
            self.loc.city_en = self.sity['name_en']
            self.loc.region_ru = self.region['name_ru']
            self.loc.region_en = self.region['name_en']
            self.loc.country_ru = self.country['name_ru']
            self.loc.country_en = self.country['name_en']
            self.olds_ip.ip_1 = self.ip
            self.olds_ip.save()
            self.loc.save()
        elif not self.olds_ip.ip_2 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = TwoUserLocation.objects.get(user=self.user)
            except:
                self.loc = TwoUserLocation.objects.create(user=self.user)
            self.sity = self.data['city']
            self.region = self.data['region']
            self.country = self.data['country']
            self.loc.city_ru = self.sity['name_ru']
            self.loc.city_en = self.sity['name_en']
            self.loc.region_ru = self.region['name_ru']
            self.loc.region_en = self.region['name_en']
            self.loc.country_ru = self.country['name_ru']
            self.loc.country_en = self.country['name_en']
            self.olds_ip.ip_2 = self.ip
            self.olds_ip.save()
            self.loc.save()
        elif not self.olds_ip.ip_3 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = ThreeUserLocation.objects.get(user=self.user)
            except:
                self.loc = ThreeUserLocation.objects.create(user=self.user)
            self.sity = self.data['city']
            self.region = self.data['region']
            self.country = self.data['country']
            self.loc.city_ru = self.sity['name_ru']
            self.loc.city_en = self.sity['name_en']
            self.loc.region_ru = self.region['name_ru']
            self.loc.region_en = self.region['name_en']
            self.loc.country_ru = self.country['name_ru']
            self.loc.country_en = self.country['name_en']
            self.olds_ip.ip_3 = self.ip
            self.olds_ip.save()
            self.loc.save()
        elif self.olds_ip.ip_3 and self.olds_ip.ip_3 != self.ip and self.olds_ip.ip_2 != self.ip and self.olds_ip.ip_1 != self.ip:
            self.response = requests.get(url= "http://api.sypexgeo.net/8Dbm8/json/" + self.ip)
            self.data = self.response.json()
            try:
                self.loc = ThreeUserLocation.objects.get(user=self.user)
            except:
                self.loc = ThreeUserLocation.objects.create(user=self.user)
            self.sity = self.data['city']
            self.region = self.data['region']
            self.country = self.data['country']
            self.loc.city_ru = self.sity['name_ru']
            self.loc.city_en = self.sity['name_en']
            self.loc.region_ru = self.region['name_ru']
            self.loc.region_en = self.region['name_en']
            self.loc.country_ru = self.country['name_ru']
            self.loc.country_en = self.country['name_en']
            self.olds_ip.ip_1 = self.ip
            self.olds_ip.save()
            self.loc.save()
        else:
            pass
        return super(StatView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(StatView,self).get_context_data(**kwargs)
        context["ip"]=self.ip
        return context
