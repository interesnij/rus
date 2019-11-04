
$('#ajax').on('click', '.comment', function () {
	var item = $(this).closest(".infinite-item").attr("item-id");
	var url = $(this).parents(".infinite-item");
	$.ajax({
			url: "/main/comment/" + item + "/",
			data: {'item': item},
			cache: false,
			beforeSend: function () {
					url.find(".load_comments").html("<span style='display:flex;justify-content: center;'><img src='/static/images/loading.gif'></span>");
			},
			success: function (data) {
				url.find(".load_comments").html(data.comments);
			}
	});
	return false;
});

function remove() {
var remove = $(this);
var pk = remove.data('id');
$.ajax({
	url: "/users/delete/" + pk + "/",
	success: function (data) {
		$(remove).parents('.card').hide();
    $('.activefullscreen').hide();
		$.toast({
				heading: '{{ request.user.first_name }}',
				text: 'статья успешно удалена!',
				showHideTransition: 'fade',
				icon: 'error'
		})
	},
	error: function(data) {
	}
});
};
$('[data-action="remove"]').click(remove);

$('.stream').on('click', '.article_detail', function (e) {
	e.preventDefault();
	 var item = $(this);
	 var item_id = item.data("id");
	 $('#article_loader').html('').load("/article/detail/" + item_id)
	 $('.article_fullscreen').show();
});


$('.stream').on('click', '.fullscreen', function () {
	 var item = $(this);
	 var item_id = item.data("id");
	 $('#item_loader').html('').load("/users/item/" + item_id)
	 $('.item_fullscreen').show();
});


function fixed() {
var fixed = $(this);
var pk = fixed.parent().data('id');
$.ajax({
	url: "/users/fixed/" + pk + "/",
	success: function (data) {
		fixed.parent().html("<span data-action='item_unfixed' style='cursor:pointer' class='dropdown-item'>Открепить</span>");
		$.toast({
				heading: '{{ request.user.first_name }}',
				text: 'Вы успешно закрепили элемент!',
				showHideTransition: 'fade',
				icon: 'info'
		})
	},
	error: function(data) {
		console.log("Что то пошло не так");
	}
});
};

function unfixed() {
var unfixed = $(this);
var pk = unfixed.parent().data('id');
$.ajax({
	url: "/users/unfixed/" + pk + "/",
	success: function (data) {
		unfixed.parent().html("<span data-action='item_fixed' style='cursor:pointer' class='dropdown-item'>Закрепить</span>");
		$.toast({
				heading: '{{ request.user.first_name }}',
				text: 'Вы успешно открепили элемент!',
				showHideTransition: 'fade',
				icon: 'info'
		})
	},
	error: function(data) {
		console.log("Что то пошло не так");
	}
});
};
$('[data-action="item_fixed"]').click(fixed);
$('[data-action="item_unfixed"]').click(unfixed);


	$('.stream').on('click', '.emoji', function () {
			var react = $(this);
			var item = react.parents('.infinite-item').attr("item-id");
			var pk = react.data('id');
			payload = {
					'item': item,
					'csrf_token': csrftoken
				}
			$.ajax({
					url: "/main/react/" + item + "/" + pk + "/",
					type: 'POST',
					cache: false,
					data: payload,
					success: function(data) {
							react.find("[data-count='react']").text(data.react_count);
							react.parents('.infinite-item').find(".reactions_stream").prepend(data);
							$(react).siblings('.reaction_window').html('').load("/main/react_window/" + item + "/");
							$.toast({
									heading: '{{ request.user.first_name }}',
									text: 'Ваша реакция засчитана',
									showHideTransition: 'fade',
									icon: 'info'
							})
					},
					error: function(data) {
						$.toast({
								heading: '{{ request.user.first_name }}',
								text: 'Вы уже отреагировали этим смайлом',
								showHideTransition: 'fade',
								icon: 'error'
						})
					}
			});
			return false;
	});


  $('.item_fullscreen_hide').on('click', function () {
  	 $('.item_fullscreen').hide();
  	 $('#item_loader').empty();
  });

  $('.stream').on('click', '.itemComment', function () {
  button1 = $(this);
  form1 = button1.parent().parent().parent();
        $.ajax({
            url: '{% url "post_comment" %}',
            data: form1.serialize(),
            type: 'POST',
            cache: false,
            success: function(data) {
                $(".form-control-rounded").val("");
                $(".stream_comments").append(data);
            },
            error: function(data) {
              $.toast({
                  heading: '{{ request.user.first_name }}',
                  text: 'Для публикации комментария нужно написать что-нибудь и/или вставить изображение(ия)',
                  showHideTransition: 'fade',
                  icon: 'error'
              })
            },
        });
        return false;
    });

  $('.stream').on('click', '.replyComment', function () {
  button = $(this);
  form = button.parent().parent().parent().parent();
        $.ajax({
            url: '{% url "reply_comment" %}',
            data: form.serialize(),
            type: 'POST',
            cache: false,
            success: function(data) {
                $(".form-control-rounded").val("");
                $(".stream_reply_comments").append(data);
                $.toast({
                    heading: '{{ request.user.first_name }}',
                    text: 'Ответ успешно создан!',
                    showHideTransition: 'fade',
                    icon: 'link'
                })
            },
            error: function(data) {
              $.toast({
                  heading: '{{ request.user.first_name }}',
                  text: 'Для публикации ответа нужно написать что-нибудь и/или вставить изображение(ия)',
                  showHideTransition: 'fade',
                  icon: 'error'
              })
            },
        });
        return false;
    });

  $('.stream').on('click', '.replyParentComment', function () {
  button = $(this);
  form = button.parent().parent().parent().parent();
        $.ajax({
            url: '{% url "reply_comment" %}',
            data: form.serialize(),
            type: 'POST',
            cache: false,
            success: function(data) {
                $(".form-control-rounded").val("");
                $(".stream_reply_comments").append(data);
                $.toast({
                    heading: '{{ request.user.first_name }}',
                    text: 'Ответ успешно создан!',
                    showHideTransition: 'fade',
                    icon: 'link'
                })
            },
            error: function(data) {
              $.toast({
                  heading: '{{ request.user.first_name }}',
                  text: 'Для публикации ответа нужно написать что-нибудь и/или вставить изображение(ия)',
                  showHideTransition: 'fade',
                  icon: 'error'
              })
            },
        });
        return false;
    });

	$( ".stream" ).on('click', '.reply_comment', function () {
    var reply_comment_form = $(this);
    var objectUser = reply_comment_form.prev().text().trim();
    var form = reply_comment_form.next().find(".text-comment");
    form.val(objectUser + ', ');
		reply_comment_form.next().show();
    form.focus();
	})


	var infinite = new Waypoint.Infinite({
	    element: $('.infinite-container')[0],
	    onBeforePageLoad: function() {
	        $('.load').show();
	    },
	    onAfterPageLoad: function($items) {
	        $('.load').hide();
	    }
	});
