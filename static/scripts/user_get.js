on('#ajax', 'click', '.avatar_detail', function() {
  uuid = this.getAttribute('photo-uuid');
  loader = document.getElementById("photo_loader");
  open_fullscreen("/gallery/load/avatar_detail/" + uuid + "/", loader)
});

on('#ajax', 'click', '.fullscreen', function() {
  var container, uuid, pk, loader;
  container = this.parentElement;
  uuid = container.getAttribute('data-uuid');
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("item_loader");
  open_fullscreen("/users/detail/post/" + pk + "/" + uuid + "/", loader)
})

on('#ajax', 'click', '.u_article_detail', function() {
  uuid = this.parentElement.getAttribute("data-uuid");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("article_loader");
  open_fullscreen("/article/detail/" + pk + "/" + uuid + "/", loader)
});

on('#ajax', 'click', '#article_add', function() {
  var pk = this.getAttribute('data-pk');
  open_fullscreen("/article/u_article_window/" + pk + "/", document.getElementById("create_loader"));
  //setTimeout(function() { CKEDITOR.replace('id_content'); CKEDITOR.instances.id_content.updateElement(); }, 1000);
});

on('#ajax', 'click', '.u_all_posts_likes', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/posts/item_window/all_user_like/" + uuid + "/", loader)
});
on('#ajax', 'click', '.u_all_posts_dislikes', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/posts/item_window/all_user_dislike/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_all_posts_comment_likes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/posts/item_window/all_user_comment_like/" + pk + "/", loader)
});
on('#ajax', 'click', '.u_all_posts_comment_dislikes', function() {
  container = this.parentElement.parentElement.parentElement;
  pk = container.getAttribute('data-pk');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/posts/item_window/all_user_comment_dislike/" + pk + "/", loader)
});

on('#ajax', 'click', '.u_all_item_reposts', function() {
  container = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = container.getAttribute('data-uuid');
  loader = document.getElementById("votes_loader");
  open_fullscreen("/posts/item_window/all_user_reposts/" + uuid + "/", loader)
});

on('#ajax', 'click', '.u_item_comments', function() {
  clear_comment_dropdown();
  parent = this.parentElement.parentElement.parentElement.parentElement;
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  uuid = parent.getAttribute("data-uuid");
  //this.parentElement.parentElement.nextElementSibling.classList.toggle("comments_open");
  url = "/posts/user/comment/" + uuid + "/" + pk + "/";
  list_load(parent.querySelector(".u_load_comments"), url);
  this.classList.toggle("comments_open");
});
