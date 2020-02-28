from users.models import User
from communities.models import Community
from django.views.generic import ListView
from common.checkers import check_is_not_blocked_with_user_with_id, check_is_connected_with_user_with_id
from main.models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.shortcuts import render_to_response
from rest_framework.exceptions import PermissionDenied

class UserCommunitiesList(View):
	def get(self, request, *args, **kwargs):
		context = {}
		template = None
		self.user=User.objects.get(uuid=self.kwargs["uuid"])
		popular_list = Community.get_trending_communities_for_user_with_id(user_id=self.user.pk)
		if self.user != request.user and request.user.is_authenticated:
			check_is_not_blocked_with_user_with_id(user=request.user, user_id=self.user.id)
			if self.user.is_closed_profile():
				check_is_connected_with_user_with_id(user=request.user, user_id=self.user.id)
			communities_list = Community.objects.filter(memberships__user__id=self.user.pk)
			template = 'user_community/communities_list.html'
		elif request.user.is_anonymous and self.user.is_closed_profile():
			raise PermissionDenied('Это закрытый профиль. Только его друзья могут видеть его информацию.')
		elif request.user.is_anonymous and not self.user.is_closed_profile():
			communities_list = Community.objects.filter(memberships__user__id=self.user.pk).order_by('-created')
			template = 'user_community/communities_list.html'
		elif self.user == request.user:
			communities_list = Community.objects.filter(memberships__user__id=self.user.pk)
			template = 'user_community/communities_list.html'

		current_page = Paginator(communities_list, 3)
		page = request.GET.get('page')
		context['user'] = self.user
		try:
			context['communities_list'] = current_page.page(page)
		except PageNotAnInteger:
			context['communities_list'] = current_page.page(1)
		except EmptyPage:
			context['communities_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template, context)


class UserManageCommunitiesList(View):
	def get(self, request, *args, **kwargs):
		context = {}
		template = "user_community/communities_list_with_staffed.html"
		self.user=User.objects.get(uuid=self.kwargs["uuid"])
		if self.user ==request.user:
			manage_communities_list = self.user.get_staffed_communities()
		else:
			manage_communities_list = ""
		current_page = Paginator(manage_communities_list, 15)
		page = request.GET.get('page')
		context['user'] = self.user
		try:
			context['manage_communities_list'] = current_page.page(page)
		except PageNotAnInteger:
			context['manage_communities_list'] = current_page.page(1)
		except EmptyPage:
			context['manage_communities_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template, context)


class UserMusicList(View):
	def get(self, request, *args, **kwargs):
		context = {}
		template = None
		self.user=User.objects.get(uuid=self.kwargs["uuid"])
		if self.user != request.user and request.user.is_authenticated:
			check_is_not_blocked_with_user_with_id(user=request.user, user_id=self.user.id)
			if self.user.is_closed_profile():
				check_is_connected_with_user_with_id(user=request.user, user_id=self.user.id)
			music_list = list(reversed(self.user.get_music()))
			template = 'user_music/music_list.html'
		elif request.user.is_anonymous and self.user.is_closed_profile():
			raise PermissionDenied('Это закрытый профиль. Только его друзья могут видеть его информацию.')
		elif request.user.is_anonymous and not self.user.is_closed_profile():
			music_list = list(reversed(self.user.get_music()))
			template = 'user_music/music_list.html'
		elif self.user == request.user:
			music_list = list(reversed(self.user.get_my_music()))
			template = 'user_music/my_music_list.html'
		current_page = Paginator(music_list, 15)
		page = request.GET.get('page')
		context['user'] = self.user
		context['request_user'] = request.user
		try:
			context['music_list'] = current_page.page(page)
		except PageNotAnInteger:
			context['music_list'] = current_page.page(1)
		except EmptyPage:
			context['music_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template, context)


class AllPossibleUsersList(View):
	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_authenticated:
			possible_list = request.user.get_possible_friends()
			current_page = Paginator(possible_list, 15)
			page = request.GET.get('page')
		else:
			possible_list = None
		context['request_user'] = request.user

		try:
			context['possible_list'] = current_page.page(page)
		except PageNotAnInteger:
			context['possible_list'] = current_page.page(1)
		except EmptyPage:
			context['possible_list'] = current_page.page(current_page.num_pages)
		return render_to_response('possible_list.html', context)


class ItemListView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		template = None
		user=User.objects.get(pk=self.kwargs["pk"])
		try:
			fixed = Item.objects.get(creator__id=user.pk, is_fixed=True)
		except:
			fixed = None
		if user != request.user and request.user.is_authenticated:
			check_is_not_blocked_with_user_with_id(user=request.user, user_id=user.id)
			if user.is_closed_profile():
				check_is_connected_with_user_with_id(user=request.user, user_id=user.id)
			items_list = user.get_posts().order_by('-created')
			template = 'lenta/item_list.html'
		elif request.user.is_anonymous and user.is_closed_profile():
			raise PermissionDenied('Это закрытый профиль. Только его друзья могут видеть его информацию.')
		elif request.user.is_anonymous and not user.is_closed_profile():
			items_list = user.get_posts().order_by('-created')
			template = 'lenta/item_list_anon.html'
		elif user == request.user:
			items_list = user.get_posts().order_by('-created')
			template = 'lenta/my_item_list.html'
		current_page = Paginator(items_list, 15)
		context['request_user'] = request.user
		context['user'] = user
		context['object'] = fixed
		page = request.GET.get('page')
		try:
			context['items_list'] = current_page.page(page)
		except PageNotAnInteger:
			context['items_list'] = current_page.page(1)
		except EmptyPage:
			context['items_list'] = current_page.page(current_page.num_pages)

		return render_to_response(template, context)


class AllUsers(ListView):
	template_name="all_users.html"
	model=User
	paginate_by=30

	def get_queryset(self):
		items = User.objects.only("pk")
		return items
