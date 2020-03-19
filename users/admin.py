from django.contrib import admin
from users.models import User
from users.model.profile import *
from users.model.settings import UserItemNotifications, UserPrivate, UserColorSettings
from users.model.list import UserBlock


class UserNotificationsSettingsInline(admin.TabularInline):
    model = UserItemNotifications

class UserPrivateSettingsInline(admin.TabularInline):
    model = UserPrivate

class UserColorSettingsInline(admin.TabularInline):
    model = UserColorSettings

class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserNotificationsSettingsInline,
        UserPrivateSettingsInline,
        UserColorSettingsInline,
    ]
    search_fields = ('last_name','first_name')



admin.site.register(User, UserAdmin)

admin.site.register(UserBlock)
admin.site.register(OneUserLocation)
admin.site.register(TwoUserLocation)
admin.site.register(ThreeUserLocation)
admin.site.register(IPUser)
admin.site.register(UserProfile)
