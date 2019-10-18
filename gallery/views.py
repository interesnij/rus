from django.views.generic.base import TemplateView
from users.models import User
from gallery.models import Album, Photo


class GalleryView(TemplateView):
	template_name="gallery.html"

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		return super(GalleryView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(GalleryView,self).get_context_data(**kwargs)
		context['user'] = self.user
		return context


class AjaxPhotoUploadView(TemplateView):

    def post_ajax(self, request, *args, **kwargs):
        try:
            album = Album.objects.get(pk=kwargs.get('pk'))
        except Album.DoesNotExist:
            error_dict = {'message': 'Album not found.'}
            return self.render_json_response(error_dict, status=404)

        uploaded_file = request.FILES['file']
        Photo.objects.create(album=album, file=uploaded_file)

        response_dict = {
            'message': 'File uploaded successfully!',
        }

        return self.render_json_response(response_dict, status=200)
