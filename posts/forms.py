from posts.models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostHardForm(forms.ModelForm):
	content_hard = forms.CharField(widget=CKEditorUploadingWidget, label='')

	class Meta:
		model = Post
		fields = ['content_hard']

class PostMediumForm(forms.ModelForm):
	content_medium = forms.CharField(widget=CKEditorUploadingWidget, label='')

	class Meta:
		model = Post
		exclude = ['content_hard','content_lite','created','creator','comments_enabled','community','is_edited','is_closed','is_deleted','views']

class PostLiteForm(forms.ModelForm):
	content_lite = forms.CharField(widget=CKEditorUploadingWidget, label='')

	class Meta:
		model = Post
		fields = ['content_lite']
