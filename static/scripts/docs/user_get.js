on('#ajax', 'click', '.u_copy_doc_list', function() {
  on_off_list_in_collections(this, "/docs/user_progs/add_list_in_collections/", "u_uncopy_doc_list", "u_copy_doc_list", "Удалить")
});
on('#ajax', 'click', '.u_uncopy_doc_list', function() {
  on_off_list_in_collections(this, "/docs/user_progs/remove_list_from_collections/", "u_copy_doc_list", "u_uncopy_doc_list", "Добавить")
});

on('#ajax', 'click', '.u_doc_list_add', function() {
  loader = document.getElementById("create_loader");
  open_fullscreen("/docs/user_progs/add_list/" + document.body.querySelector(".pk_saver").getAttribute("data-pk") + "/", loader)
});

on('#ajax', 'click', '.u_doc_add', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("create_loader");
  open_fullscreen("/docs/user_progs/create_doc/", loader);
});

on('#ajax', 'click', '.u_doc_list_edit_window', function() {
  body = document.body.querySelector(".pk_saver");
  pk = body.getAttribute("data-pk");
  uuid = body.getAttribute("data-uuid");
  loader = document.getElementById("create_loader");
  open_fullscreen("/docs/user_progs/edit_list/" + pk + "/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_load_doc_list', function() {
  parent = this.parentElement.parentElement.parentElement;
  uuid = parent.getAttribute("data-uuid"); pk = parent.getAttribute("data-pk");
  loader = document.getElementById("item_loader");
  open_fullscreen("/docs/user/load/" + pk + "/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_ucm_doc_repost', function() {
  parent = this.parentElement;
  doc_pk = parent.getAttribute("doc-pk");
  parent.getAttribute('data-pk') ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/docs/repost/u_ucm_doc_window/" + pk + "/" + doc_pk + "/", loader);
  clear_attach_block();
})
on('#ajax', 'click', '.u_ucm_doc_list_repost', function() {
  parent = this.parentElement.parentElement.parentElement;
  parent.getAttribute("data-pk") ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  parent.getAttribute("data-uuid") ? uuid = parent.getAttribute('data-uuid') : uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/docs/repost/u_ucm_list_window/" + pk + "/" + uuid + "/", loader);
  clear_attach_block();
})
