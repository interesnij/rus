on('#ajax', 'click', '.u_photoComment', function() {
  form = this.parentElement.parentElement.parentElement;
  send_comment(form, form.parentElement.previousElementSibling, '/gallery/user_progs/post-comment/');
});

on('#ajax', 'click', '.u_replyPostComment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  send_comment(form, form.parentElement.parentElement.querySelector(".stream_reply_comments"), '/gallery/user_progs/reply-comment/')
  form.parentElement.style.display = "none";
});

on('#ajax', 'click', '.u_replyParentPostComment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  send_comment(form, form.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement, '/gallery/user_progs/reply-comment/')
  form.parentElement.style.display = "none";
});

on('#ajax', 'click', '.photo_user_off_comment', function() {
  send_change(this, "/gallery/user_progs/off_comment/", "photo_user_on_comment", "Включить комментарии")
})
on('#ajax', 'click', '.photo_user_on_comment', function() {
  send_change(this, "/gallery/user_progs/on_comment/", "photo_user_off_comment", "Выключить комментарии")
})

on('#ajax', 'click', '.u_photo_like', function() {
  photo = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = photo.getAttribute("photo-uuid");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_like(item, "/gallery/votes/user_like/" + uuid + "/" + pk + "/");
  vote_reload("/gallery/photo_window/u_like_window/" + uuid + "/", "/gallery/photo_window/u_dislike_window/" + uuid + "/", this.nextElementSibling, this.nextElementSibling.nextElementSibling.nextElementSibling)
});
on('#ajax', 'click', '.u_photo_dislike', function() {
  photo = this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  uuid = photo.getAttribute("photo-uuid");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_dislike(item, "/gallery/votes/user_dislike/" + uuid + "/" + pk + "/");
  vote_reload("/gallery/photo_window/u_like_window/" + uuid + "/", "/gallery/photo_window/u_dislike_window/" + uuid + "/", this.previousElementSibling, this.nextElementSibling)
});
on('#ajax', 'click', '.u_photo_dislike2', function() {
  _this = this;
  photo = _this.parentElement;
  comment_pk = photo.getAttribute("data-pk");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_like(item, "/gallery/votes/user_comment/" + comment_pk + "/" + pk + "/like/");
  vote_reload("/gallery/photo_window/u_comment_like_window/" + comment_pk + "/", "/gallery/photo_window/u_comment_dislike_window/" + comment_pk + "/", _this.nextElementSibling, _this.nextElementSibling.nextElementSibling.nextElementSibling)
});
on('#ajax', 'click', '.u_photo_dislike2', function() {
  _this = this;
  photo = _this.parentElement;
  comment_pk = photo.getAttribute("data-pk");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_dislike(item, "/gallery/votes/user_comment/" + comment_pk + "/" + pk + "/dislike/");
  vote_reload("/gallery/photo_window/u_comment_like_window/" + comment_pk + "/", "/gallery/photo_window/u_comment_dislike_window/" + comment_pk + "/", _this.previousElementSibling, _this.nextElementSibling)
});
