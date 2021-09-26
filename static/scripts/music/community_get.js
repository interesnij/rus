on('#ajax', 'click', '.c_copy_playlist', function() {
  on_off_list_in_collections(this, "/music/community_progs/add_list_in_collections/", "c_uncopy_playlist", "c_copy_playlist", "Удалить")
});
on('#ajax', 'click', '.c_uncopy_playlist', function() {
  on_off_list_in_collections(this, "/music/community_progs/remove_list_from_collections/", "c_copy_playlist", "c_uncopy_playlist", "Добавить")
});

on('#ajax', 'click', '.c_ucm_music_repost', function() {
  parent = this.parentElement;
  track_pk = parent.getAttribute("data-pk");
  parent.getAttribute('data-pk') ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  create_fullscreen("/music/repost/c_ucm_music_window/" + pk + "/" + track_pk + "/", "worker_fullscreen");
  clear_attach_block();
})
on('#ajax', 'click', '.c_ucm_music_list_repost', function() {
  parent = this.parentElement.parentElement.parentElement;
  parent.getAttribute("data-pk") ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  parent.getAttribute("data-uuid") ? uuid = parent.getAttribute('data-uuid') : uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  create_fullscreen("/music/repost/c_ucm_list_window/" + pk + "/" + uuid + "/", "worker_fullscreen");
  clear_attach_block();
})

on('#ajax', 'click', '.c_soundcloud_set_create', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  create_fullscreen("/music/community_progs/souncloud_create_list_window/" + pk + "/", "worker_fullscreen");
});

on('#ajax', 'click', '.c_soundcloud_set_list', function() {
  uuid = this.parentElement.parentElement.getAttribute('data-uuid');
  create_fullscreen("/music/community_progs/souncloud_list_window/" + uuid + "/", "worker_fullscreen");
});
on('#ajax', 'click', '.c_music_list_create_window', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  create_fullscreen("/music/community_progs/create_list_window/" + pk + "/", "worker_fullscreen");
});

on('#ajax', 'click', '.c_playlist_edit', function() {
  uuid = this.parentElement.parentElement.getAttribute('data-uuid');
  create_fullscreen("/music/community_progs/edit_list/" + uuid + "/", "worker_fullscreen");
});

on('#ajax', 'click', '.c_track_add', function() {
  create_fullscreen("/music/community_progs/add_track/", "worker_fullscreen");
});
on('#ajax', 'click', '.c_playlist_add', function() {
  create_fullscreen("/music/community_progs/add_list/" + document.body.querySelector(".pk_saver").getAttribute('data-pk') + "/", "worker_fullscreen");
});
