on('#ajax', 'click', '.u_copy_good_list', function() {
  on_off_list_in_collections(this, "/goods/user_progs/add_list_in_collections/", "u_uncopy_good_list", "u_copy_good_list", "Удалить")
});
on('#ajax', 'click', '.u_uncopy_good_list', function() {
  on_off_list_in_collections(this, "/goods/user_progs/remove_list_from_collections/", "u_copy_good_list", "u_uncopy_good_list", "Добавить")
});

on('#ajax', 'click', '.load_profile_good_list', function() {
  profile_list_block_load(this, ".load_block", "/goods_list/", "load_profile_good_list");
});

on('#ajax', 'click', '.load_attach_good_list', function() {
  profile_list_block_attach(this, ".load_block", "/u_good_list_load/", "load_attach_good_list");
});

on('#ajax', 'click', '.u_good_detail', function() {
  this.getAttribute('data-uuid') ? uuid = this.getAttribute('data-uuid') : uuid = this.parentElement.parentElement.getAttribute('data-uuid')
  pk = this.getAttribute('good-pk');
  loader = document.getElementById("good_loader");
  open_fullscreen('/goods/user/good/' + pk + '/' + uuid + '/', loader);
  setTimeout(function() {good_gallery(loader)}, 1000)
});

on('#ajax', 'click', '.u_ucm_good_repost', function() {
  parent = this.parentElement.parentElement.parentElement.parentElement.parentElement
  good_pk = block.getAttribute("good-pk");
  parent.getAttribute('data-pk') ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/repost/u_ucm_good_window/" + pk + "/" + good_pk + "/", loader);
  clear_attach_block();
})
on('#ajax', 'click', '.u_ucm_good_list_repost', function() {
  parent = this.parentElement.parentElement.parentElement;
  parent.getAttribute("data-pk") ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  parent.getAttribute("data-uuid") ? uuid = parent.getAttribute('data-uuid') : uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/repost/u_ucm_list_window/" + pk + "/" + uuid + "/", loader);
  clear_attach_block();
})

on('#ajax', 'click', '.u_good_list_add', function() {
  loader = document.getElementById("create_loader");
  open_fullscreen("/goods/user_progs/add_list/" + document.body.querySelector(".pk_saver").getAttribute("data-pk") + "/", loader)
});
on('#ajax', 'click', '.u_good_list_edit', function() {
  uuid = this.parentElement.parentElement.getAttribute('data-uuid');
  loader = document.getElementById("create_loader");
  open_fullscreen("/goods/user_progs/edit_list/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_goods_list_create', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("create_loader");
  open_fullscreen("/goods/user_progs/add_list/" + pk + "/", loader)
});
on('#ajax', 'click', '.u_all_good_likes', function() {
  pk = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('good-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_like/" + pk + "/", loader)
});
on('#ajax', 'click', '.u_all_good_dislikes', function() {
  pk = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('good-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_dislike/" + pk + "/", loader)
});

on('#ajax', 'click', '.u_all_good_comment_likes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_comment_like/" + pk + "/", loader)
});
on('#ajax', 'click', '.u_all_good_comment_dislikes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_comment_dislike/" + pk + "/", loader)
});

on('#ajax', 'click', '.u_all_good_reposts', function() {
  pk = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('good-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_reposts/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_good_comments', function() {
  clear_comment_dropdown();
  block = this.parentElement.parentElement.parentElement.parentElement.parentElement;
  pk = block.getAttribute("data-pk");
  good_pk = block.getAttribute("good-pk");
  block_comments = block.querySelector(".u_load_comments");
  if (block_comments.classList.contains("show")){
    block_comments.classList.remove("show")
  } else {
    block_comments.firstChild ? null : list_load(block_comments, "/goods/user/comment/" + uuid + "/" + pk + "/");
    block_comments.classList.add("show")
  }
});

on('#ajax', 'click', '.load_good_list', function() {
  parent = this.parentElement.parentElement.parentElement;
  loader = document.getElementById("item_loader");
  open_fullscreen("/goods/load_list/" + parent.getAttribute("data-pk") + "/", loader)
});
