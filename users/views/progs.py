from django.views import View
from users.models import User
from django.http import HttpResponse
from django.http import Http404
from common.templates import render_for_platform


class UserBanCreate(View):
    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax():
            request.user.block_user_with_pk(self.user.pk)
            return HttpResponse()

class UserUnbanCreate(View):
    def get(self,request,*args,**kwargs):
        self.user = User.objects.get(pk=self.kwargs["pk"])
        if request.is_ajax():
            request.user.unblock_user_with_pk(self.user.pk)
            return HttpResponse()
        else:
            raise Http404

class UserColorChange(View):
    def get(self,request,*args,**kwargs):
        from users.model.settings import UserColorSettings

        if not request.is_ajax():
            raise Http404
        try:
            model = UserColorSettings.objects.get(user=request.user)
        except:
            model = UserColorSettings.objects.create(user=request.user)
        color = self.kwargs["color"]
        if model.color == color:
            return HttpResponse('Этот цвет уже выбран')
        else:
            model.color = color
            model.save(update_fields=['color'])
            return HttpResponse('Цвет выбран')


class PhoneVerify(View):
    def get(self,request,*args,**kwargs):
        from common.model.other import PhoneCodes
        from common.utils import create_user_models

        if not request.is_ajax():
            raise Http404
        code = self.kwargs["code"]
        phone = self.kwargs["phone"]
        try:
            obj = PhoneCodes.objects.get(phone=phone, code=code)
        except:
            obj = None
        if obj:
            user = User.objects.get(pk=request.user.pk)
            user.type = User.STANDART
            user.phone = obj.phone
            user.save()
            create_user_models(user)
            obj.delete()
            data = 'ok'
            response = render_for_platform(request,'generic/response/phone.html',{'response_text':data})
            return response
        else:
            data = 'Код подтверждения неверный. Проверьте, пожалуйста, номер, с которого мы Вам звонили. Последние 4 цифры этого номера и есть код подтверждения, который нужно ввести с поле "Последние 4 цифры". Если не можете найти номер, нажмите на кнопку "Перезвонить повторно".'
            response = render_for_platform(request,'generic/response/phone.html',{'response_text':data})
            return response


class PhoneSend(View):
    def get(self,request,*args,**kwargs):
        import json, requests
        from common.model.other import PhoneCodes

        text = ""
        if not request.is_ajax() and not request.user.is_no_phone_verified():
            raise Http404
        else:
            phone = self.kwargs["phone"]
            if len(phone) > 8:
                try:
                    user = User.objects.get(phone=phone)
                    data = 'Пользователь с таким номером уже зарегистрирован. Используйте другой номер или напишите в службу поддержки, если этот номер Вы не использовали ранее.'
                    response = render_for_platform(request,'generic/response/phone.html',{'response_text':data})
                    return response
                except:
                    response = requests.get(url="https://api.ucaller.ru/v1.0/initCall?service_id=12203&key=GhfrKn0XKAmA1oVnyEzOnMI5uBnFN4ck&phone=" + phone)
                    data = response.json()
                    PhoneCodes.objects.create(phone=phone, code=data['code'])
                    data = 'Мы Вам звоним. Последние 4 цифры нашего номера - код подтверждения, который нужно ввести в поле "Последние 4 цифры" и нажать "Подтвердить"'
                    response = render_for_platform(request,'generic/response/code_send.html',{'response_text':data})
                    return response
            else:
                data = 'Введите, пожалуйста, корректное количество цифр Вашего телефона'
                response = render_for_platform(request,'generic/response/phone.html',{'response_text':data})
                return response
