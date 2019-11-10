from django.views.generic.base import TemplateView
from users.models import User
from gallery.models import Album, Photo
from gallery.helpers import AjaxResponseMixin, JSONResponseMixin
from django.views.generic import ListView
from gallery.forms import AlbumForm
from django.http import HttpResponse, HttpResponseBadRequest


class GalleryView(TemplateView):
	template_name="gallery.html"

	def get(self,request,*args,**kwargs):
		self.user=User.objects.get(pk=self.kwargs["pk"])
		self.albums=Album.objects.filter(creator=self.user)
		return super(GalleryView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(GalleryView,self).get_context_data(**kwargs)
		context['user'] = self.user
		return context

class AlbumsListView(ListView):
	template_name="albums.html"
	model=Album
	paginate_by=10

	def get_queryset(self):
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		albums=Album.objects.filter(creator__id=self.user.id)
		return albums


class PhotosListView(ListView):
	template_name="photos.html"
	model=Photo
	paginate_by=15

	def get_queryset(self):
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		photos=Photo.objects.filter(creator__id=self.user.id)
		return photos


class AlbomView(TemplateView):
	template_name="album.html"

	def get(self,request,*args,**kwargs):
		self.album=Album.objects.get(uuid=self.kwargs["uuid"])
		self.photos = Photo.objects.filter(album=self.album)
		return super(AlbomView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AlbomView,self).get_context_data(**kwargs)
		context['album'] = self.album
		context['photos'] = self.photos
		return context


class AlbomReloadView(TemplateView):
	template_name="album_reload.html"

	def get(self,request,*args,**kwargs):
		self.album=Album.objects.get(uuid=self.kwargs["uuid"])
		self.photos = Photo.objects.filter(album=self.album)
		return super(AlbomReloadView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AlbomReloadView,self).get_context_data(**kwargs)
		context['album'] = self.album
		context['photos'] = self.photos
		return context


class PhotoUserCreate(AjaxResponseMixin,JSONResponseMixin,TemplateView):
	template_name="add_photos.html"

	def post_ajax(self, request, *args, **kwargs):
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		try:
			self.album = Album.objects.get(pk=self.kwargs["pk"])
		except:
			self.album = None

		uploaded_file = request.FILES['file']
		Photo.objects.create(album=self.album, file=uploaded_file, creator=self.user)

		response_dict = {'message': 'File uploaded successfully!',}
		return self.render_json_response(response_dict, status=200)


class AlbumUserCreate(TemplateView):
	template_name="add_album.html"
	form=None

	def get(self,request,*args,**kwargs):
		self.form=AlbumForm()
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		return super(AlbumUserCreate,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AlbumUserCreate,self).get_context_data(**kwargs)
		context["form"]=self.form
		context["user"]=self.user
		return context

	def post(self,request,*args,**kwargs):
		self.form = AlbumForm(request.POST)
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		if self.form.is_valid():
			new_album = self.form.save(commit=False)
			new_album.creator=self.user
			new_album = self.form.save()
			if request.is_ajax() :
				return HttpResponse("!")
		else:
			return HttpResponse("!")
		return super(AlbumUserCreate,self).get(request,*args,**kwargs)


class AlbomGygView(TemplateView):
	template_name="gygyg.html"

	def get(self,request,*args,**kwargs):
		self.user = User.objects.get(uuid=self.kwargs["uuid"])
		self.album = Album.objects.filter(creator=self.user)
		self.new_url = self.album.last().uuid
		return super(AlbomGygView,self).get(request,*args,**kwargs)

	def get_context_data(self,**kwargs):
		context=super(AlbomGygView,self).get_context_data(**kwargs)
		context["new_url"]=self.new_url
		return context
