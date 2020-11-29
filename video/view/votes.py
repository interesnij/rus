import json
from users.models import User
from video.models import Video, VideoComment
from communities.models import Community
from django.http import HttpResponse
from django.views import View
from common.model.votes import VideoVotes, VideoCommentVotes
from rest_framework.exceptions import PermissionDenied
from common.check.community import check_can_get_lists
from django.http import Http404


class VideoUserLikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.LIKE:
                likedislike.vote = VideoVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.LIKE)
            result = True
            if user != request.user:
                video.notification_user_like(request.user)
        likes = video.likes_count()
        dislikes = video.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommentUserLikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.LIKE:
                likedislike.vote = VideoCommentVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.LIKE)
            result = True
            if user != request.user:
                comment.notification_user_comment_like(request.user)
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoUserDislikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.DISLIKE:
                likedislike.vote = VideoVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.DISLIKE)
            result = True
            if user != request.user:
                video.notification_user_dislike(request.user)
        likes = item.likes_count()
        dislikes = video.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommentUserDislikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.DISLIKE:
                likedislike.vote = VideoCommentVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.DISLIKE)
            result = True
            if user != request.user:
                comment.notification_user_comment_dislike(request.user)
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommunityLikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.LIKE:
                likedislike.vote = VideoVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.LIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                video.notification_community_like(request.user)
        likes = video.likes_count()
        dislikes = video.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommunityDislikeCreate(View):
    def get(self, request, **kwargs):
        video = Video.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax() and not video.votes_on:
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = VideoVotes.objects.get(parent=video, user=request.user)
            if likedislike.vote is not VideoVotes.DISLIKE:
                likedislike.vote = VideoVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoVotes.DoesNotExist:
            VideoVotes.objects.create(parent=video, user=request.user, vote=VideoVotes.DISLIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                video.notification_community_dislike(request.user)
        likes = video.likes_count()
        dislikes = item.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommentCommunityLikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.LIKE:
                likedislike.vote = VideoCommentVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.LIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                comment.notification_community_comment_like(request.user, community)
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class VideoCommentCommunityDislikeCreate(View):
    def get(self, request, **kwargs):
        comment = VideoComment.objects.get(pk=self.kwargs["comment_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = VideoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not VideoCommentVotes.DISLIKE:
                likedislike.vote = VideoCommentVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except VideoCommentVotes.DoesNotExist:
            VideoCommentVotes.objects.create(item=comment, user=request.user, vote=VideoCommentVotes.DISLIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                comment.notification_community_comment_dislike(request.user, community)
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")
