import json
from users.models import User
from gallery.models import Photo, PhotoComment
from communities.models import Community
from notify.model.photo import *
from django.http import HttpResponse
from django.views import View
from common.model.votes import PhotoVotes, PhotoCommentVotes
from common.check.user import check_user_can_get_list
from common.check.community import check_can_get_lists
from django.http import Http404


class PhotoUserLikeCreate(View):
    def get(self, request, **kwargs):
        item = Photo.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = PhotoVotes.objects.get(parent=item, user=request.user)
            if likedislike.vote is not PhotoVotes.LIKE:
                likedislike.vote = PhotoVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoVotes.DoesNotExist:
            PhotoVotes.objects.create(parent=item, user=request.user, vote=PhotoVotes.LIKE)
            result = True
            if user.pk != request.user.pk:
                photo_notification_handler(request.user, item.creator, item, PhotoNotify.LIKE)
        likes = item.likes_count()
        dislikes = item.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoUserDislikeCreate(View):
    def get(self, request, **kwargs):
        item = Photo.objects.get(uuid=self.kwargs["uuid"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = PhotoVotes.objects.get(parent=item, user=request.user)
            if likedislike.vote is not PhotoVotes.DISLIKE:
                likedislike.vote = PhotoVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoVotes.DoesNotExist:
            PhotoVotes.objects.create(parent=item, user=request.user, vote=PhotoVotes.DISLIKE)
            result = True
            if user != request.user:
                photo_notification_handler(request.user, item.creator, item, PhotoNotify.DISLIKE)
        likes = item.likes_count()
        dislikes = item.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommentUserLikeCreate(View):
    def get(self, request, **kwargs):
        comment = PhotoComment.objects.get(pk=self.kwargs["comment_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = PhotoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not PhotoCommentVotes.LIKE:
                likedislike.vote = PhotoCommentVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoCommentVotes.DoesNotExist:
            PhotoCommentVotes.objects.create(item=comment, user=request.user, vote=PhotoCommentVotes.LIKE)
            result = True
            if user != request.user:
                if comment.parent_comment:
                    photo_comment_notification_handler(request.user, comment, PhotoNotify.LIKE_REPLY, "u_photo_reply_notify")
                else:
                    photo_comment_notification_handler(request.user, comment, PhotoNotify.LIKE_COMMENT, "u_photo_comment_notify")
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommentUserDislikeCreate(View):
    def get(self, request, **kwargs):
        comment = PhotoComment.objects.get(pk=self.kwargs["comment_pk"])
        user = User.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        if user != request.user:
            check_user_can_get_list(request.user, user)
        try:
            likedislike = PhotoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not PhotoCommentVotes.DISLIKE:
                likedislike.vote = PhotoCommentVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoCommentVotes.DoesNotExist:
            PhotoCommentVotes.objects.create(item=comment, user=request.user, vote=PhotoCommentVotes.DISLIKE)
            result = True
            if user != request.user:
                if comment.parent_comment:
                    photo_comment_notification_handler(request.user, comment, PhotoNotify.DISLIKE_REPLY, "u_photo_reply_notify")
                else:
                    photo_comment_notification_handler(request.user, comment, PhotoNotify.DISLIKE_COMMENT, "u_photo_comment_notify")
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommunityLikeCreate(View):
    def get(self, request, **kwargs):
        item = Photo.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not item.votes_on or not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = PhotoVotes.objects.get(parent=item, user=request.user)
            if likedislike.vote is not PhotoVotes.LIKE:
                likedislike.vote = PhotoVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoVotes.DoesNotExist:
            PhotoVotes.objects.create(parent=item, user=request.user, vote=PhotoVotes.LIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                photo_community_notification_handler(request.user, community, item, PhotoCommunityNotify.LIKE)
        likes = item.likes_count()
        dislikes = item.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommunityDislikeCreate(View):
    def get(self, request, **kwargs):
        item = Photo.objects.get(uuid=self.kwargs["uuid"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not item.votes_on or not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = PhotoVotes.objects.get(parent=item, user=request.user)
            if likedislike.vote is not PhotoVotes.DISLIKE:
                likedislike.vote = PhotoVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoVotes.DoesNotExist:
            PhotoVotes.objects.create(parent=item, user=request.user, vote=PhotoVotes.DISLIKE)
            result = True
            if not request.user.is_staff_of_community(community.pk):
                photo_community_notification_handler(request.user, community, item, PhotoCommunityNotify.DISLIKE)
        likes = item.likes_count()
        dislikes = item.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommentCommunityLikeCreate(View):
    def get(self, request, **kwargs):
        comment = PhotoComment.objects.get(pk=self.kwargs["comment_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = PhotoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not PhotoCommentVotes.LIKE:
                likedislike.vote = PhotoCommentVotes.LIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoCommentVotes.DoesNotExist:
            PhotoCommentVotes.objects.create(item=comment, user=request.user, vote=PhotoCommentVotes.LIKE)
            result = True
            if comment.parent_comment:
                photo_community_comment_notification_handler(request.user, community, comment, PhotoCommunityNotify.LIKE_REPLY, "c_photo_reply_notify")
            else:
                photo_community_comment_notification_handler(request.user, community, comment, PhotoCommunityNotify.LIKE_COMMENT, "c_photo_comment_notify")
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(dislikes)}),content_type="application/json")


class PhotoCommentCommunityDislikeCreate(View):
    def get(self, request, **kwargs):
        comment = PhotoComment.objects.get(pk=self.kwargs["comment_pk"])
        community = Community.objects.get(pk=self.kwargs["pk"])
        if not request.is_ajax():
            raise Http404
        check_can_get_lists(request.user,community)
        try:
            likedislike = PhotoCommentVotes.objects.get(item=comment, user=request.user)
            if likedislike.vote is not PhotoCommentVotes.DISLIKE:
                likedislike.vote = PhotoCommentVotes.DISLIKE
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except PhotoCommentVotes.DoesNotExist:
            PhotoCommentVotes.objects.create(item=comment, user=request.user, vote=PhotoCommentVotes.DISLIKE)
            result = True
            if comment.parent_comment:
                photo_community_comment_notification_handler(request.user, community, comment, PhotoCommunityNotify.DISLIKE_REPLY, "c_photo_reply_notify")
            else:
                photo_community_comment_notification_handler(request.user, community, comment, PhotoCommunityNotify.DISLIKE_COMMENT, "c_photo_comment_notify")
        likes = comment.likes_count()
        dislikes = comment.dislikes_count()
        return HttpResponse(json.dumps({"result": result,"like_count": str(likes),"dislike_count": str(disliks)}),content_type="application/json")
