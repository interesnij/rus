on('#ajax', 'click', '#c_ucm_doc_repost_btn', function() {
  repost_constructor(this,
                     "/docs/repost/c_u_doc_repost/",
                     "Репост документа на стену сделан",
                     "/docs/repost/c_c_doc_repost/",
                     "Репост документа в сообщества сделан",
                     "/docs/repost/c_m_doc_repost/",
                     "Репост документа в сообщения сделан")
});
on('#ajax', 'click', '#c_ucm_doc_list_repost_btn', function() {
  repost_constructor(this,
                     "/docs/repost/c_u_doc_list_repost/",
                     "Репост списка документов на стену сделан",
                     "/docs/repost/c_c_doc_list_repost/",
                     "Репост списка документов в сообщества сделан",
                     "/docs/repost/c_m_doc_list_repost/",
                     "Репост списка документов в сообщения сделан")
});

on('#ajax', 'click', '.c_add_doc_list', function(e) {
  _this = this;
  parent = this.parentElement.parentElement.parentElement;
  uuid = parent.getAttribute("data-uuid");
  var link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/docs/community_progs/add_list/" + uuid + "/", true );
  link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  link.onreadystatechange = function () {
    if ( link.readyState == 4 && link.status == 200 ) {
      _this.innerHTML = "";
      _this.classList.add("c_remove_doc_list");
      _this.classList.remove("c_add_doc_list")
      _this.innerHTML = '<svg fill="currentColor" class="svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"/><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/></svg>'
  }};
  link.send( null );
});
on('#ajax', 'click', '.c_remove_doc_list', function(e) {
  _this = this;
  parent = this.parentElement.parentElement.parentElement;
  uuid = parent.getAttribute("data-uuid");
  var link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/docs/community_progs/remove_list/" + uuid + "/", true );
  link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  link.onreadystatechange = function () {
    if ( link.readyState == 4 && link.status == 200 ) {
      _this.innerHTML = "";
      _this.classList.add("c_add_doc_list");
      _this.classList.remove("c_remove_doc_list")
      _this.innerHTML = '<svg fill="currentColor" class="svg_default" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/><path d="M0 0h24v24H0z" fill="none"/></svg>'
  }};
  link.send( null );
});

on('#ajax', 'click', '.c_doc_add', function() {
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  loader = document.getElementById("create_loader");
  open_fullscreen("/docs/community_progs/create_doc/" + pk + "/", loader);
});

on('#ajax', 'click', '.c_doc_remove', function(e) {
  block = this.parentElement;
  pk = block.parentElement.getAttribute("data-pk");
  uuid = document.body.querySelector(".pk_saver").getAttribute("data-uuid");
  var _link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  _link.open( 'GET', "/docs/community_progs/c_remove_doc/" + pk + "/" + uuid + "/", true );
  _link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  _link.onreadystatechange = function () {
    if ( _link.readyState == 4 && _link.status == 200 ) {
      block.innerHTML = "";
      block.innerHTML = "<span class='c_doc_add btn_default pointer' title='Добавить'><svg fill='currentColor' style='width:22px;height:22px;' class='svg_default'><path d='M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z'/><path d='M0 0h24v24H0z' fill='none'/></svg></span>"
  }};
  _link.send( null );
});

on('#ajax', 'click', '.c_add_doc_in_list', function() {
  add_item_in_list(this, '/docs/community_progs/add_doc_in_list/', "c_add_doc_in_list", "c_remove_doc_from_list")
})
on('#ajax', 'click', '.c_remove_photo_from_list', function() {
  remove_item_from_list(this, '/docs/community_progs/remove_doc_from_list/', "c_remove_doc_from_list", "c_add_doc_in_list")
})

on('#ajax', 'click', '#c_create_doc_list_btn', function() {
  form = this.parentElement.parentElement.parentElement;
  form_data = new FormData(form);
  if (!form.querySelector("#id_name").value){
    form.querySelector("#id_name").style.border = "1px #FF0000 solid";
    toast_error("Название - обязательное поле!");
  } else { this.disabled = true }
  post_and_load_object_page(form, "/docs/community_progs/add_list/", "/communities/", "/doc_list/");
});

on('#ajax', 'click', '#c_create_doc_btn', function() {
  form = document.querySelector("#c_doc_create");
  form_data = new FormData(form);

  lists = form.querySelector("#id_list");
  selectedOptions = lists.selectedOptions;
  val = false;
  for (var i = 0; i < selectedOptions.length; i++) {
    if(selectedOptions[i].value) {val = true}
  }

  if (!form.querySelector("#id_title").value){
    form.querySelector("#id_title").style.border = "1px #FF0000 solid";
    toast_error("Название - обязательное поле!")
  } else if (!val){
    form.querySelector("#id_list").style.border = "1px #FF0000 solid";
    toast_error("Выберите список!")
  }
  else if (!form.querySelector("#id_file").value){
    form.querySelector("#id_file").style.border = "1px #FF0000 solid";
    toast_error("Загрузите документ!")
  } else { this.disabled = true }
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  uuid = document.body.querySelector(".pk_saver").getAttribute("data-uuid");
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/docs/community_progs/create_doc/" + pk + "/", true );
  link_.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    elem = link_.responseText;
    response = document.createElement("span");
    response.innerHTML = elem;
    list = document.body.querySelector("#id_list");
    span1 = response.querySelector('.span1')
    if (span1.classList.contains(uuid)){
      container = document.body.querySelector(".is_paginate");
      container.insertAdjacentHTML('afterBegin', response.innerHTML);
      container.querySelector(".doc_empty") ? container.querySelector(".doc_empty").style.display = "none" : null;
      toast_info("Документ создан!")
    } else{
      toast_info("Документ создан!")
    }
    close_create_window();
  }};

  link_.send(form_data);
});

on('#ajax', 'click', '#u_edit_doc_list_btn', function() {
  media_list_edit(this, "/docs/community_progs/edit_list/")
});

on('body', 'click', '.c_doc_list_remove', function() {
  media_list_delete(this, "/docs/community_progs/delete_list/", "c_doc_list_remove", "c_doc_list_abort_remove")
});
on('body', 'click', '.c_doc_list_abort_remove', function() {
  media_list_recover(this, "/docs/community_progs/restore_list/", "c_doc_list_abort_remove", "c_doc_list_remove")
});
