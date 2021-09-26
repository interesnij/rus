on('#ajax', 'click', '.c_video_list_add', function() {
  loader = document.getElementById("create_loader");
  create_fullscreen("/video/community_progs/add_list/" + document.body.querySelector(".pk_saver").getAttribute('data-pk') + "/", "worker_fullscreen");
});
on('#ajax', 'click', '.c_video_add', function() {
  create_fullscreen("/video/community_progs/create_video/", "item_fullscreen");
});
on('#ajax', 'click', '.c_copy_video_list', function() {
  on_off_list_in_collections(this, "/video/community_progs/add_list_in_collections/", "c_uncopy_video_list", "c_copy_video_list", "Удалить")
});
on('#ajax', 'click', '.c_uncopy_video_list', function() {
  on_off_list_in_collections(this, "/video/community_progs/remove_list_from_collections/", "c_copy_video_list", "c_uncopy_video_list", "Добавить")
});

on('#ajax', 'click', '.c_ucm_video_list_repost', function() {
  parent = this.parentElement.parentElement.parentElement;
  parent.getAttribute("data-pk") ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  parent.getAttribute("data-uuid") ? uuid = parent.getAttribute('data-uuid') : uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  create_fullscreen("/video/repost/c_ucm_video_list_window/" + pk + "/" + uuid + "/", "worker_fullscreen");
  clear_attach_block();
})
on('#ajax', 'click', '.c_ucm_video_repost', function() {
  parent = this.parentElement;
  track_pk = parent.getAttribute("data-pk");
  parent.getAttribute('data-pk') ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  create_fullscreen("/video/repost/c_ucm_video_window/" + pk + "/" + track_pk + "/", "worker_fullscreen");
  clear_attach_block();
})
on('#ajax', 'click', '.c_ucm_video_list_repost', function() {
  parent = this.parentElement;
  parent.getAttribute("data-pk") ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  parent.getAttribute("data-uuid") ? uuid = parent.getAttribute('data-uuid') : uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  create_fullscreen("/video/repost/c_ucm_video_list_window/" + pk + "/" + uuid + "/", "worker_fullscreen");
  clear_attach_block();
})

on('#ajax', 'click', '.с_video_list_create', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  create_fullscreen("/video/community_progs/add_list/" + pk + "/", "worker_fullscreen");
});

on('#ajax', 'click', '.c_video_list_edit', function() {
  uuid = this.parentElement.parentElement.getAttribute('data-uuid');
  create_fullscreen("/video/community_progs/edit_list/" + uuid + "/", "worker_fullscreen");
});

on('#video_loader', 'click', '.c_all_video_likes', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  create_fullscreen("/video/window/all_community_like/" + uuid + "/", "worker_fullscreen");
});
on('#video_loader', 'click', '.c_all_video_dislikes', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  create_fullscreen("/video/window/all_community_dislike/" + uuid + "/", "worker_fullscreen");
});

on('#video_loader', 'click', '.c_all_video_comment_likes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  create_fullscreen("/video/window/all_community_comment_like/" + pk + "/", "worker_fullscreen");
});
on('#video_loader', 'click', '.c_all_video_comment_dislikes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  create_fullscreen("/video/window/all_community_comment_dislike/" + pk + "/", "worker_fullscreen");
});

on('#video_loader', 'click', '.c_all_video_reposts', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  create_fullscreen("/video/window/all_community_reposts/" + uuid + "/", "worker_fullscreen");
});

on('#video_loader', 'click', '.c_video_comments', function() {
  clear_comment_dropdown();
  video_display = this.parentElement.parentElement.parentElement;
  pk = video_display.getAttribute("data-pk");
  uuid = video_display.getAttribute("data-uuid");
  block_comments = video_display.nextElementSibling;
  if (block_comments.classList.contains("show")){
    block_comments.classList.remove("show")
  } else {
    block_comments.firstChild ? null : list_load(block_comments, "/video/community/comment/" + uuid + "/" + pk + "/");
    block_comments.classList.add("show")
  }
});

on('#ajax', 'click', '.c_video_list_detail', function() {
  video_pk = this.getAttribute("video-pk");
  counter = this.getAttribute('video-counter') - 1;
  pk = this.getAttribute('data-pk');
  play_video_list("/video/community/list/" + pk + "/", counter, video_pk)
});

on('#ajax', 'click', '.c_post_video', function() {
  video_pk = this.getAttribute("video-pk");
  uuid = this.parentElement.parentElement.parentElement.getAttribute("video-pk");
  counter = this.getAttribute('video-counter') - 1;
  play_video_list("/video/community/list_post/" + uuid + "/", counter, video_pk)
});
