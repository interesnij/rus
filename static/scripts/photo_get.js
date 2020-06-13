on('#ajax', 'click', '.u_album_photo_detail', function() {
  container = this.parentElement;
  uuid = document.body.querySelector(".pk_saver").getAttribute('data-uuid');
  uuid2 = container.getAttribute('data-uuid2');
  pk = this.getAttribute('photo-pk');
  loader = document.getElementById("photo_loader");
  open_fullscreen("/gallery/load/u_album_photo/" + pk + "/" + uuid + "/" + uuid2 + "/", loader)
});
on('#ajax', 'click', '.u_photo_detail', function() {
  var container, uuid, pk, loader;
  container = this.parentElement;
  pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  uuid = this.getAttribute('photo-uuid');
  loader = document.getElementById("photo_loader");
  open_fullscreen("/gallery/load/u_photo/" + pk + "/" + uuid + "/", loader)
});
on('#ajax', 'click', '.u_photos_add', function() {
  document.querySelector('#photos_add_window').style.display =="none";
})

on('#ajax', 'click', '.u_albums_add', function() {
  var container, uuid, loader;
  container = this.parentElement;
  pk = document.body.querySelector(".pk_saver").getAttribute('data-pk');
  loader = document.getElementById("create_loader");
  open_fullscreen("/gallery/user/add_album/" + pk + "/", loader)
});

on('#ajax', 'click', '.u_photo_edit', function() {
  document.querySelector('#block_description_form').style.display =="none";
})

  link_.send(form_data);
});

on('#ajax', 'click', '#add_album', function() {
  form = document.body.querySelector("#form_album_add");
  form_data = new FormData(form);
  if (!form.querySelector("#id_title").value){
    form.querySelector("#id_title").style.border = "1px #FF0000 solid";
    toast_error("Название - обязательное поле!");
  } else { null }
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");

  var ajax_link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
    ajax_link.open( 'POST', "/gallery/user/add_album/" + pk + "/", true );
    ajax_link.onreadystatechange = function () {
      if ( this.readyState == 4 && this.status == 200 ) {
        elem_ = document.createElement('span');
        elem_.innerHTML = ajax_link.responseText;
        ajax = elem_.querySelector("#reload_block");
        rtr = document.getElementById('ajax');
        rtr.innerHTML = ajax.innerHTML;
        uuid = rtr.querySelector(".pk_saver").getAttribute("album-uuid");
        window.scrollTo(0,0);
        document.title = elem_.querySelector('title').innerHTML;
        window.history.pushState(null, "vfgffgfgf", '/gallery/user/album/' + pk + '/' + uuid + '/');
        toast_info("Альбом изображений создан!");
        album_photo_load =  rtr.querySelector("#album_photo_load");
        list_load(album_photo_load, album_photo_load.getAttribute("data-link"));
      }
    }
    ajax_link.send(form_data);
});
