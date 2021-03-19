def linebreaks(value, autoescape=None):
    from django.utils.html import linebreaks
    from django.utils.safestring import mark_safe
    autoescape = autoescape and not isinstance(value, SafeData)
    return mark_safe(linebreaks(value, autoescape))


def get_post(user, value):
    block = ''
    #try:
    from posts.models import Post
    post = Post.objects.get(pk=value, is_deleted=False)
    if post.votes_on:
        votes_on = ''
    else:
        votes_on = 'style="display:none"'
    if post.comments_enabled:
        comments_enabled = ''
    else:
        comments_enabled = 'style="display:none"'
    user_like, user_dislikes = "btn_default", "btn_default"

    if post.community:
        if post.is_have_likes():
            if post.likes().filter(user_id=user.pk).exists():
                user_like = "btn_success"
            window_likes = '<div class="like_pop"><span class="c_all_posts_likes pointer">Оценили: ' + post.likes_count_ru() + '</span><span style="display: flex;margin-top: 10px;">'
            for i in post.window_likes():
                window_likes = ''.join([window_likes, '<a href="', i.user.get_link(), '" class="ajax" style="padding-right:10px" data-pk="', \
                str(i.user.pk), '"><figure style="margin: 0;" title="', i.user.get_full_name(), '"><img src="', "", '" \
                style="border-radius: 50px;width:50px;" alt="image"></figure></a>'])
            window_likes += '</span></div>'
        else:
            window_likes = ''
        if post.is_have_dislikes():
            if post.dislikes().filter(user_id=user.pk).exists():
                user_dislikes = "btn_danger"
            window_dislikes = '<div class="dislike_pop"><span class="c_all_posts_dislikes pointer">Не оценили: ' + post.dislikes_count_ru() + '</span><span style="display: flex;margin-top: 10px;">'
            for i in post.window_dislikes():
                window_dislikes = ''.join([window_dislikes, '<a href="', i.user.get_link(), '" class="ajax" style="padding-right:10px" data-pk="', \
                str(i.user.pk), '"><figure style="margin: 0;" title="', i.user.get_full_name(), '"><img src="', i.user.get_avatar(), '" \
                style="border-radius: 50px;width:50px;" alt="image"></figure></a>'])
            window_dislikes += '</div></span>'
        else:
            window_dislikes = ''
        if post.attach:
            attach = post.get_c_attach(user)
        else:
            attach = ''
        community = post.community
        if user.is_administrator_of_community(community.pk):
            card_drop = '<span class="dropdown-item c_post_remove">Удалить</span>'
        elif user.is_post_manager():
            card_drop = '<span class="dropdown-item post_delete_window">♦ Удалить</span>'
        else:
            card_drop = '<span class="dropdown-item post_claim">Пожаловаться</span>'
        return ''.join([block, '<span data-pk="', str(community.pk), '"list-pk="', str(post.get_list_pk()), '" data-uuid="', str(post.uuid), '"><div class="card-header">\
        <div class="media"><a href="', community.get_link(), '" class="ajax"><figure>', community.get_community_avatar(), '</figure></a><div class="media-body"><h6 class="mb-0"><a href="', community.get_link(), '" class="ajax">\
        ', community.name, '</a></h6><p class="mb-0">', post.get_created(), '</p></div><div class="dropdown"><a style="cursor:pointer" class="icon-circle icon-30 btn_default drop">\
        <svg class="svg_info" fill="currentColor" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>\
        </a><div class="dropdown-menu dropdown-menu-right"><span><span class="dropdown-item u_all_posts_likes pointer">Оценили</span>\
        <span class="dropdown-item c_all_posts_dislikes pointer">Не оценили</span></span>', card_drop, '</div></div></div></div>\
         <div class="c_fullscreen pointer">', linebreaks(post.text),'\
        </div>', attach, '<div class="card-footer border-top py-2"><div class="row"><div class="col interaction" id="interaction">\
        <span ', votes_on, ' class="like c_like ', user_like, '" title="Нравится"><svg class="svg_info" fill="currentColor"viewBox="0 0 24 24">\
        <path fill="none" d="M0 0h24v24H0V0z"/><path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z"/>\
        </svg><span class="likes_count" data-count="like">', str(post.likes_count()), '</span></span><span class="like_window">', window_likes, '</span><span ', votes_on, ' class="dislike \
        c_dislike ', user_dislikes, '" title="Не нравится"><svg class="svg_info" fill="currentColor" viewBox="0 0 24 24">\
        <path fill="none" d="M0 0h24v24H0z"/><path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"/>\
        </svg><span class="dislikes_count">', str(post.dislikes_count()), '</span></span><span class="dislike_window">', window_dislikes, '</span><span title="Комментарий" \
        class="c_item_comments btn_default" style="cursor:pointer;margin-right: 5px;', comments_enabled, '"><svg class="svg_info" \
        fill="currentColor" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/>\
        <path d="M0 0h24v24H0z" fill="none"/></svg><span class="comment-count">', str(post.count_comments()), '</span></span>\
        <span title="Поделиться" class="u_ucm_post_repost btn_default pointer"><svg class="svg_info" fill="currentColor" \
        viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/>\
        </svg><span class="repost_count">', str(post.count_reposts()), '</span></span></div><span class="col-auto" title="Просмотры" \
        style="font-size:12px"><svg fill="currentColor" class="svg_info svg_default" style="width:17px;padding-bottom: 3px;" \
        viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>\
        </svg>', str(post.all_visits_count()), '</span></div><div class="c_load_comments"></div></div></span>'])

    else:
        if post.is_have_likes():
            if post.likes().filter(user_id=user.pk).exists():
                user_like = "btn_success"
            window_likes = '<div class="like_pop"><span class="u_all_posts_likes pointer">Оценили: ' + post.likes_count_ru() + '</span><span style="display: flex;margin-top: 10px;">'
            for i in post.window_likes():
                window_likes = ''.join([window_likes, '<a href="', i.user.get_link(), '" class="ajax" style="padding-right:10px" data-pk="', \
                str(i.user.pk), '"><figure style="margin: 0;" title="', i.user.get_full_name(), '"><img src="', i.user.get_avatar(), '" \
                style="border-radius: 50px;width:50px;" alt="image"></figure></a>'])
            window_likes += '</span></div>'
        else:
            window_likes = ''
        if post.is_have_dislikes():
            if post.dislikes().filter(user_id=user.pk).exists():
                user_dislikes = "btn_danger"
            window_dislikes = '<div class="dislike_pop"><span class="u_all_posts_dislikes pointer">Не оценили: ' + post.dislikes_count_ru() + '</span><span style="display: flex;margin-top: 10px;">'
            for i in post.window_dislikes():
                window_dislikes = ''.join([window_dislikes, '<a href="', i.user.get_link(), '" class="ajax" style="padding-right:10px" data-pk="', \
                str(i.user.pk), '"><figure style="margin: 0;" title="', i.user.get_full_name(), '"><img src="', i.user.get_avatar(), '" \
                style="border-radius: 50px;width:50px;" alt="image"></figure></a>'])
            window_dislikes += '</div></span>'
        else:
            window_dislikes = ''
        if post.attach:
            attach = post.get_u_attach(user)
        else:
            attach = ''
        creator = post.creator
        if post.creator.pk == user.pk:
            card_drop = '<span class="dropdown-item u_post_remove">Удалить</span>'
        elif user.is_post_manager():
            card_drop = '<span class="dropdown-item post_delete_window">♦ Удалить</span>'
        else:
            card_drop = '<span class="dropdown-item post_claim">Пожаловаться</span>'
        return ''.join([block, '<span data-pk="', str(creator.pk), '"list-pk="', str(post.get_list_pk()), '" data-uuid="', str(post.uuid), '"><div class="card-header">\
        <div class="media"><a href="', creator.get_link(), '" class="ajax"><figure>', creator.get_my_avatar(), '</figure></a><div class="media-body"><h6 class="mb-0"><a href="', creator.get_link(), '" class="ajax">\
        ', creator.get_full_name(), '</a></h6><p class="mb-0">', post.get_created(), '</p></div><div class="dropdown"><a style="cursor:pointer" class="icon-circle icon-30 btn_default drop">\
        <svg class="svg_info" fill="currentColor" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>\
        </a><div class="dropdown-menu dropdown-menu-right"><span><span class="dropdown-item u_all_posts_likes pointer">Оценили</span>\
        <span class="dropdown-item u_all_posts_dislikes pointer">Не оценили</span></span>', card_drop, '</div></div></div></div>\
         <div class="fullscreen pointer">', linebreaks(post.text),'\
        </div>', attach, '<div class="card-footer border-top py-2"><div class="row"><div class="col interaction" id="interaction">\
        <span ', votes_on, ' class="like u_like ', user_like, '" title="Нравится"><svg class="svg_info" fill="currentColor"viewBox="0 0 24 24">\
        <path fill="none" d="M0 0h24v24H0V0z"/><path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z"/>\
        </svg><span class="likes_count" data-count="like">', str(post.likes_count()), '</span></span><span class="like_window">', window_likes, '</span><span ', votes_on, ' class="dislike \
        u_dislike ', user_dislikes, '" title="Не нравится"><svg class="svg_info" fill="currentColor" viewBox="0 0 24 24">\
        <path fill="none" d="M0 0h24v24H0z"/><path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z"/>\
        </svg><span class="dislikes_count">', str(post.dislikes_count()), '</span></span><span class="dislike_window">', window_dislikes, '</span><span title="Комментарий" \
        class="u_item_comments btn_default" style="cursor:pointer;margin-right: 5px;', comments_enabled, '"><svg class="svg_info" \
        fill="currentColor" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/>\
        <path d="M0 0h24v24H0z" fill="none"/></svg><span class="comment-count">', str(post.count_comments()), '</span></span>\
        <span title="Поделиться" class="u_ucm_post_repost btn_default pointer"><svg class="svg_info" fill="currentColor" \
        viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92 1.61 0 2.92-1.31 2.92-2.92s-1.31-2.92-2.92-2.92z"/>\
        </svg><span class="repost_count">', str(post.count_reposts()), '</span></span></div><span class="col-auto" title="Просмотры" \
        style="font-size:12px"><svg fill="currentColor" class="svg_info svg_default" style="width:17px;padding-bottom: 3px;" \
        viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>\
        </svg>', str(post.all_visits_count()), '</span></div><div class="u_load_comments"></div></div></span>'])
    #except:
    #    pass
