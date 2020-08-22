on('#ajax', 'click', '.u_good_detail', function() {

  document.body.querySelector(".pk_saver") ? pk = document.body.querySelector(".pk_saver").getAttribute('data-pk') : pk = this.getAttribute('data-pk');
  uuid = this.getAttribute('good-uuid');
  loader = document.getElementById("good_loader");
  open_fullscreen('/goods/user/good/' + pk + '/' + uuid + '/', loader);
  setTimeout(function() {good_gallery(loader)}, 1000)
});

on('#ajax', 'click', '.u_ucm_good_repost', function() {
  parent = this.parentElement.parentElement.parentElement.parentElement.parentElement
  uuid = parent.getAttribute("data-uuid");
  parent.getAttribute('data-pk') ? pk = parent.getAttribute('data-pk') : pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/repost/u_ucm_good_window/" + pk + "/" + uuid + "/", loader);
  clear_attach_block();
})

on('#ajax', 'click', '.u_all_good_likes', function() {
  uuid = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_like/" + uuid + "/", loader)
});
on('#ajax', 'click', '.u_all_good_dislikes', function() {
  uuid = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_dislike/" + uuid + "/", loader)
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
  uuid = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/goods/window/all_user_reposts/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_good_comments', function() {
  clear_comment_dropdown();
  block = this.parentElement.parentElement.parentElement.parentElement.parentElement;
  pk = block.getAttribute("data-pk");
  uuid = block.getAttribute("data-uuid");
  url = "/goods/user/comment/" + uuid + "/" + pk + "/";
  list_load(block.querySelector(".u_load_comments"), url);
  this.classList.toggle("comments_open");
});
