on('#ajax', 'click', '.copy_community_music_list', function() {
  on_off_list_in_collections(this, "/music/community_progs/add_list_in_collections/", "uncopy_community_music_list", "copy_community_music_list", "Удалить")
});
on('#ajax', 'click', '.uncopy_community_music_list', function() {
  on_off_list_in_collections(this, "/music/community_progs/remove_list_from_collections/", "copy_community_music_list", "uncopy_community_music_list", "Добавить")
});

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
  pk = this.parentElement.parentElement.getAttribute('data-pk');
  create_fullscreen("/music/community_progs/edit_list/" + pk + "/", "worker_fullscreen");
});

on('#ajax', 'click', '.c_track_add', function() {
  create_fullscreen("/music/community_progs/add_track/", "worker_fullscreen");
});
on('#ajax', 'click', '.c_playlist_add', function() {
  create_fullscreen("/music/community_progs/add_list/" + document.body.querySelector(".pk_saver").getAttribute('data-pk') + "/", "worker_fullscreen");
});
