/*!
   item post scripts for user
  */

  $("body").on('click', '.u_like', function() {
      like = $(this); item = like.parents('.infinite-item');pk = item.attr("user-id");uuid = item.attr("item-id");dislike = like.next().next();
      $.ajax({url: "/votes/user_like/" + uuid + "/" + pk + "/",type: 'POST',data: {'obj': pk},
          success: function(json) {
              like.find("[data-count='like']").text(json.like_count); like.toggleClass('svg_success'); like.find(".likes_count").toggleClass('svg_success'); like.next().html('').load("/window/u_like_window/" + uuid + "/" + pk + "/");
              dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.removeClass('svg_danger'); dislike.find(".dislikes_count").removeClass('svg_danger'); dislike.next().html('').load("/window/u_dislike_window/" + uuid + "/" + pk + "/")
          }
      });return false;
  });
  $("body").on('click', '.u_dislike', function() {
          dislike = $(this); item = dislike.parents('.infinite-item');pk = item.attr("user-id");uuid = item.attr("item-id");like = dislike.prev().prev();
          $.ajax({
              url: "/votes/user_dislike/" + uuid + "/" + pk + "/", type: 'POST', data: {'obj': pk},
              success: function(json) {
                like.find("[data-count='like']").text(json.like_count); like.removeClass('svg_success'); like.find(".likes_count").removeClass('svg_success'); like.next().html('').load("/window/u_like_window/" + uuid + "/" + pk + "/");
                dislike.find("[data-count='dislike']").text(json.dislike_count); dislike.find(".svg_default").toggleClass('svg_danger'); dislike.toggleClass('svg_danger'); dislike.next().html('').load("/window/u_dislike_window/" + uuid + "/" + pk + "/")
              }
          });return false;
  });
