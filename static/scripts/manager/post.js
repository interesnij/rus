on('#ajax', 'click', '.post_suspend_window', function() {
  _this = this;
  if(_this.parentElement.classList.contains("btn_console")){
    div = _this.parentElement.parentElement.parentElement.parentElement;
    uuid = _this.parentElement.parentElement.parentElement.parentElement.getAttribute("data-uuid");
    list = document.querySelectorAll('.pag');
    for (var i = 0; i < list.length; i++) {
      list[i].classList.remove("changed");
    }
    div.classList.add("changed")
  }else if (_this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute){
    uuid = _this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute("data-uuid");
  }
  loader = document.getElementById("create_loader");
  open_fullscreen("/managers/progs_post/suspend_window/" + uuid, loader)
})
on('#ajax', 'click', '.post_delete_window', function() {
  _this = this;
  if(_this.parentElement.classList.contains("btn_console")){
    div = _this.parentElement.parentElement.parentElement.parentElement;
    uuid = _this.parentElement.parentElement.parentElement.parentElement.getAttribute("data-uuid");
    list = document.querySelectorAll('.pag');
    for (var i = 0; i < list.length; i++) {
      list[i].classList.remove("changed");
    }
    div.classList.add("changed")
  }else if (_this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute){
    uuid = _this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute("data-uuid");
  }
  loader = document.getElementById("create_loader");
  open_fullscreen("/managers/progs_post/delete_window/" + uuid, loader)
})

on('#ajax', 'click', '.create_post_suspend_btn', function() {
  _this = this;
  form_data = new FormData(document.querySelector("#post_suspend_form"));
  form_post = document.querySelector("#post_suspend_form");
  if (document.body.querySelector(".changed")){
    div = document.body.querySelector(".changed");
    pk = div.getAttribute("data-uuid");
    moderation_container = document.body.querySelector("#moderation_post_container");
  } else if (_this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute){
    div = _this.parentElement.parentElement.parentElement.parentElement.parentElement;
    pk = div.getAttribute("data-uuid");
    container_object = document.body.querySelector(".post_container");
  }

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/managers/progs_post/create_suspension/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Пост заморожен!");
    document.querySelector(".create_fullscreen").style.display = "none";
    document.getElementById("create_loader").innerHTML="";
    div.remove();
    if (container_object){
      container_object.querySelector(".card") ? container_object.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Пока ничего нет...</h6></div>' : null;
      console.log(container_object);
    }else if (moderation_container){
      moderation_container.querySelector(".pag") ? moderation_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Жалоб пока нет...</h6></div>' : null;
      console.log(moderation_container);
    }
    console.log(moderation_container);
    console.log(container_object);
  }};
  link_.send(form_data);
});

on('#ajax', 'click', '.create_post_delete_btn', function() {
  var moderation_container, container_object, _this;

  _this = this;
  form_data = new FormData(document.querySelector("#post_delete_form"));
  form_post = document.querySelector("#post_delete_form");
  if (document.body.querySelector(".changed")){
    div = document.body.querySelector(".changed");
    pk = div.getAttribute("data-uuid");
    moderation_container = document.body.querySelector("#moderation_post_container");
  } else if (_this.parentElement.parentElement.parentElement.parentElement.parentElement.getAttribute){
    div = _this.parentElement.parentElement.parentElement.parentElement.parentElement;
    pk = div.getAttribute("data-uuid");
    container_object = document.body.querySelector(".post_container");
  }

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/managers/progs_post/create_delete/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Пост удален!");
    document.querySelector(".create_fullscreen").style.display = "none";
    document.getElementById("create_loader").innerHTML="";
    div.remove();
    if (container_object){
      container_object.querySelector(".card") ? container_object.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Пока ничего нет...</h6></div>' : null;
      console.log(container_object);
    }else if (moderation_container){
      moderation_container.querySelector(".pag") ? moderation_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Жалоб пока нет...</h6></div>' : null;
      console.log(moderation_container);
    }
    console.log(moderation_container);
    console.log(container_object);
  }};

  link_.send(form_data);
});

on('#ajax', 'click', '.post_unverify', function() {
  div = this.parentElement.parentElement.parentElement.parentElement;
  post_uuid = div.getAttribute("data-uuid");
  obj_pk = div.getAttribute("data-pk");
  penalty_container = document.body.querySelector("#penalty_post_container");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/managers/progs_post/unverify/" + post_uuid + "/" + obj_pk + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Верификация отменена!");
    div.remove();
    if (penalty_container){
      penalty_container.querySelector(".pag") ? penalty_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Штраф-лист пуст...</h6></div>' : null
    }
  }};

  link_.send();
});

on('#ajax', 'click', '.remove_post_suspend', function() {
  div = this.parentElement.parentElement.parentElement.parentElement;
  uuid = div.getAttribute("data-uuid");
  penalty_container = document.body.querySelector("#penalty_post_container");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/managers/progs_post/delete_suspension/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Заморозка отменена!");
    div.remove();
    if (penalty_container){
      penalty_container.querySelector(".pag") ? penalty_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Штраф-лист пуст...</h6></div>' : null
    }
  }};
  link_.send();
});
on('#ajax', 'click', '.remove_post_delete', function() {
  div = this.parentElement.parentElement.parentElement.parentElement;
  uuid = div.getAttribute("data-uuid");
  penalty_container = document.body.querySelector("#penalty_post_container");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/managers/progs_post/delete_delete/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Пост разблокирован!");
    div.remove();
    if (penalty_container){
      penalty_container.querySelector(".pag") ? penalty_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Штраф-лист пуст...</h6></div>' : null
    }
  }};
  link_.send();
});

on('#ajax', 'click', '.post_rejected', function() {
  div = this.parentElement.parentElement.parentElement.parentElement;
  uuid = div.getAttribute("data-uuid");
  moderation_container = document.body.querySelector("#moderation_post_container");

  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'GET', "/managers/progs_post/create_rejected/" + uuid + "/", true );

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    toast_info("Жалобы на запись удалены!");
    div.remove();
    if (moderation_container){
      moderation_container.querySelector(".card") ? moderation_container.innerHTML = '<div class="card mb-3 post_empty centered"><div class="card-body"><svg fill="currentColor" class="thumb_big svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path fill="currentColor" d="M22 13h-8v-2h8v2zm0-6h-8v2h8V7zm-8 10h8v-2h-8v2zm-2-8v6c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V9c0-1.1.9-2 2-2h6c1.1 0 2 .9 2 2zm-1.5 6l-2.25-3-1.75 2.26-1.25-1.51L3.5 15h7z"/></svg></div><h6 style="margin: 20px;text-align: center;"> Пока ничего нет...</h6></div>' : null
    }
  }};

  link_.send();
});
