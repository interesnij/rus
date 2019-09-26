from django.views.generic.base import TemplateView
from posts.forms import PostHardForm, PostLiteForm, PostMediumForm
from users.models import User
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.helpers import ajax_required, AuthorRequiredMixin
from posts.models import Post
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods


class PostsView(TemplateView):
    template_name="posts.html"


class PostUserHardCreate(TemplateView):
    template_name="post_hard_add.html"
    form=None
    success_url="/"

    def get(self,request,*args,**kwargs):
        self.form=PostHardForm(initial={"creator":request.user})
        return super(PostUserHardCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostUserHardCreate,self).get_context_data(**kwargs)
        context["form_hard"]=self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form=PostHardForm(request.POST)
        if self.form.is_valid():
            new_post=self.form.save(commit=False)
            new_post.creator=self.request.user
            new_post=self.form.save()

            if request.is_ajax() :
                 html = render_to_string('profile/post.html',{'object': new_post,'request': request})
                 return HttpResponse(html)
        return super(PostUserHardCreate,self).get(request,*args,**kwargs)

class PostUserMediumCreate(TemplateView):
    template_name="post_medium_add.html"
    form=None
    success_url="/"

    def get(self,request,*args,**kwargs):
        self.form=PostMediumForm(initial={"creator":self.request.user})
        return super(PostUserMediumCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostUserMediumCreate,self).get_context_data(**kwargs)
        context["form_medium"]=self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form=PostMediumForm(request.POST)
        if self.form.is_valid():
            new_post=self.form.save(commit=False)
            new_post.creator=self.request.user
            new_post=self.form.save()

            if request.is_ajax() :
                 html = render_to_string('profile/post.html',{'object': new_post,'request': request})
                 return HttpResponse(html)
        return super(PostUserMediumCreate,self).get(request,*args,**kwargs)

class PostUserLiteCreate(TemplateView):
    template_name="post_lite_add.html"
    form=None
    success_url="/"

    def get(self,request,*args,**kwargs):
        self.form=PostLiteForm(initial={"creator":request.user})
        return super(PostUserLiteCreate,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostUserLiteCreate,self).get_context_data(**kwargs)
        context["form_lite"]=self.form
        return context

    def post(self,request,*args,**kwargs):
        self.form=PostLiteForm(request.POST,request.FILES)
        if self.form.is_valid():
            new_post=self.form.save(commit=False)
            new_post.creator=self.request.user
            new_post=self.form.save()

            if request.is_ajax() :
                 html = render_to_string('profile/post.html',{'object': new_post,'request': request})
                 return HttpResponse(html)
        return super(PostUserLiteCreate,self).get(request,*args,**kwargs)

class PostDeleteView(TemplateView):
    success_url = '/'
    template_name="post_confirm_delete.html"

    def get(self,request,*args,**kwargs):
        post = Post.objects.get(pk=self.kwargs["pk"])
        if post.creator == self.request.user:
            post.is_deleted=True
            post.save()
            return HttpResponse("!")
        return super(PostDeleteView,self).get(request,*args,**kwargs)


class PostLikeView(TemplateView):
    template_name="post_like_window.html"

    def get(self,request,*args,**kwargs):
        self.post_like = Post.objects.get(pk=self.kwargs["pk"])
        self.post_like.notification_like(request.user)
        return super(PostLikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostLikeView,self).get_context_data(**kwargs)
        context["post_like"]=self.post_like
        return context

class PostDislikeView(TemplateView):
    template_name="post_dislike_window.html"

    def get(self,request,*args,**kwargs):
        self.post_dislike = Post.objects.get(pk=self.kwargs["pk"])
        self.post_dislike.notification_dislike(request.user)
        return super(PostDislikeView,self).get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context=super(PostDislikeView,self).get_context_data(**kwargs)
        context["post_dislike"]=self.post_dislike
        return context


@login_required
@require_http_methods(["GET"])
def get_thread(request):

    post_id = request.GET['post']
    post = Post.objects.get(uuid=post_id)
    posts_html = render_to_string("generic/post.html", {"object": post})
    thread_html = render_to_string(
        "generic/post_thread.html", {"thread": post.get_thread()})
    return JsonResponse({
        "uuid": post_id,
        "post": posts_html,
        "thread": thread_html,
    })

@login_required
@require_http_methods(["POST"])
def post_comment(request):

    user = request.user
    post = request.POST['reply']
    par = request.POST['parent']
    parent = Post.objects.get(pk=par)
    post = post.strip()
    if post:
        parent.reply_this(user, post)
        return JsonResponse({'comments': parent.count_thread()})

    else:
        return HttpResponseBadRequest()

@login_required
@require_http_methods(["POST"])
def update_interactions(request):
    data_point = request.POST['id_value']
    post = Post.objects.get(uuid=data_point)
    data = {'likes': post.count_likers(), 'dislikes': post.count_dislikers(), 'comments': post.count_thread()}
    return JsonResponse(data)
