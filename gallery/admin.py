from django.contrib import admin
from gallery.models import PhotoList, Photo


class PhotoListAdmin(admin.ModelAdmin):
    list_display = ['name', 'creator', 'community', 'type', 'created']
    list_filter = ['creator', ]
    class Meta:
        model = PhotoList

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['creator','community', 'created']
    list_filter = ['creator', ]

    class Meta:
            model = Photo

admin.site.register(PhotoList, PhotoListAdmin)
admin.site.register(Photo, PhotoAdmin)
