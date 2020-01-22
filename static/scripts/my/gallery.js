
$('#ajax').on('click', '.photo_detail', function() {
    photo = $(this); photo_id = photo.data("id"); user_uuid = photo.data("uuid");
    $('#photo_loader').html('').load("/gallery/load/photo/" + photo_id + "/" + user_uuid + "/")
    $('.photo_fullscreen').show();
});

$('#ajax').on('click', '.album_photo_detail', function() {
    photo = $(this); pk = photo.data("pk"); uuid = photo.parent().data("uuid"); uuid2 = photo.parent().data("uuid2");
    $('#photo_loader').html('').load("/gallery/load/u_photo/" + pk + "/" + uuid + "/" + uuid2 + "/")
    $('.photo_fullscreen').show();
});

$('#ajax').on('click', '.photos_add', function() { $('#photos_add_window').show(); })
$('#ajax').on('click', '.albums_add', function() { var user = $(this); var user_id = user.data("uuid"); $('#photo_add_loader').html('').load("/gallery/user/add_album/" + user_id + "/"); $('.add_fullscreen').show(); })
$('#ajax').on('click', '.add_fullscreen_hide', function() { $('.add_fullscreen').hide(); $('#photo_loader').empty(); });
$('#ajax').on('click', '.photo_fullscreen_hide', function() { $('.photo_fullscreen').hide(); $('#photo_loader').empty(); });
