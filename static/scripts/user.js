
on('#ajax', 'click', '.color_change', function() {
  var span = this;
  var color = this.getAttribute('data-color');
  var input = span.querySelector(".custom-control-input");
  var list = document.querySelector(".theme-color");
  var link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/users/progs/color/" + color + "/", true );
  link_.send();
  link_.onreadystatechange = function () {
  if ( link_.readyState == 4 && link_.status == 200 ) {
    var uncheck=document.getElementsByTagName('input');
    for(var i=0;i<uncheck.length;i++)
    {uncheck[i].checked=false;}
    input.checked = true;
    addStyleSheets("/static/styles/color/" + color + ".css");
  }
};
});

on('#ajax', 'click', '#holder_article_image', function() {
  img = this.previousElementSibling.querySelector("#id_g_image")
  get_image_priview(this, img);
});

on('#ajax', 'click', '.user_claim', function() {
  this.parentElement.classList.remove("show");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("worker_loader");
  open_fullscreen("/managers/progs_user/claim_window/" + pk, loader)
})
on('#ajax', 'click', '.create_user_claim_btn', function() {
  form_data = new FormData(document.querySelector("#user_claim_form"));
  form_post = document.querySelector("#user_claim_form");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/managers/progs_user/create_claim/" + pk + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Жалоба отправлена!");
    document.querySelector(".worker_fullscreen").style.display = "none";
    document.getElementById("worker_loader").innerHTML="";
  }};
  link_.send(form_data);
});

on('#ajax', 'click', '.post_claim', function() {
  uuid = this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute("data-uuid");
  loader = document.getElementById("worker_loader");
  open_fullscreen("/managers/progs_post/claim_window/" + uuid, loader)
})
on('#ajax', 'click', '.create_post_claim_btn', function() {
  uuid = this.getAttribute("data-uuid");
  form_data = new FormData(document.querySelector("#post_claim_form"));
  form_post = document.querySelector("#post_claim_form");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/managers/progs_post/create_claim/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Жалоба отправлена!");
    document.querySelector(".worker_fullscreen").style.display = "none";
    document.getElementById("worker_loader").innerHTML="";
  }};
  link_.send(form_data);
});

on('#ajax', 'click', '.follow_create', function() {
  document.body.querySelector(".pk_saver") ?  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk") : null
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.timeout = 30000;
  link_.open( 'GET', "/follows/add/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    this_page_reload('/users/' + pk + '/');
    toast_info("Подписка оформлена!");
  }};
  link_.send();
})
on('#ajax', 'click', '.follow_delete', function() {
  _this = this;
  document.body.querySelector(".pk_saver") ? pk = document.body.querySelector(".pk_saver").getAttribute("data-pk")
                                           : pk = _this.parentElement.parentElement.parentElement.getAttribute("data-pk");
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.timeout = 30000;
  link_.addEventListener('loadstart', _loadstart);
  link_.open( 'GET', "/follows/delete/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    document.body.querySelector(".pk_saver") ? (this_page_reload('/users/' + pk + '/'), toast_info("Друг добавлен!"))
          : (_this.parentElement.parentElement.parentElement.remove(),
            block = document.body.querySelector("#followings_container"),
            !block.querySelector(".pag") ? block.innerHTML = '<div class="card centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/><path d="M0 0h24v24H0z" fill="none"/></svg></div><h6 style="margin: 20px;text-align: center;"> Заявок нет...</h6></div>' : null)
  }};
  link_.ontimeout = function() {alert( 'Извините, запрос превысил максимальное время' )}

  function _loadstart() {console.log("Запрос начат")}
  link_.send();
})
on('#ajax', 'click', '.follow_view', function() {
  _this = this;
  document.body.querySelector(".pk_saver") ?  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk") : null
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/follows/view/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    _this.remove();
    toast_info("Пользователь оставлен в подписчиках");
  }};
  link_.send();
})

on('#ajax', 'click', '.connect_create', function() {
  document.body.querySelector(".pk_saver") ? pk = document.body.querySelector(".pk_saver").getAttribute("data-pk")
                                           : pk = this.parentElement.parentElement.parentElement.getAttribute("data-pk");
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );

  link_.open( 'GET', "/friends/add/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    document.body.querySelector(".pk_saver") ? (this_page_reload('/users/' + pk + '/'), toast_info("Друг добавлен!"))
        : (_this.parentElement.parentElement.parentElement.remove(),
          block = document.body.querySelector("#followings_container"),
          !block.querySelector(".pag") ? block.innerHTML = '<div class="card centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/><path d="M0 0h24v24H0z" fill="none"/></svg></div><h6 style="margin: 20px;text-align: center;"> Подписчиков нет...</h6></div>' : null)
  }};
  link_.send();
})
on('#ajax', 'click', '.connect_delete', function() {
  document.body.querySelector(".pk_saver") ?  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk") : null
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/friends/delete/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    document.body.querySelector(".pk_saver") ? (this_page_reload('/users/' + pk + '/'), toast_info("Друг удален!"))
                                             : null
  }};
  link_.send();
})
on('#ajax', 'click', '.user_block', function() {
  document.body.querySelector(".pk_saver") ?  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk") : null
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.timeout = 30000;
  link_.open( 'GET', "/users/progs/block/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    this_page_reload('/users/' + pk + '/');
    toast_info("Пользователь заблокирован!");
  }};
  link_.send();
})
on('#ajax', 'click', '.user_unblock', function() {
  document.body.querySelector(".pk_saver") ?  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk") : null
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.timeout = 30000;
  link_.open( 'GET', "/users/progs/unblock/" + pk + "/", true );
  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    this_page_reload('/users/' + pk + '/');
    toast_info("Пользователь разблокирован!");
  }};
  link_.send();
})
