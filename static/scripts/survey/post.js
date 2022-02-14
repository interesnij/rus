on('#ajax', 'click', '#add_survey_btn', function() {
  form_post = this.parentElement.parentElement.parentElement;
  form_data = new FormData(form_post);

  answers = form_post.querySelector("#answers_container");
  selectedOptions = answers.querySelectorAll(".answer");
  val = false;
  for (var i = 0; i < selectedOptions.length; i++) {
    if(selectedOptions[i].value) {val = true}
  }
  if (!document.body.querySelector("#id_title").value){
    document.body.querySelector("#id_title").style.border = "1px #FF0000 solid";
    toast_error("Название - обязательное поле!");
  } else if (!val){
    for (var i = 0; i < selectedOptions.length; i++) {selectedOptions[i].style.border = "1px #FF0000 solid"};
    toast_error("Задайте варианты ответов!");
    return
  } else {this.disabled = true}
  link_ = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link_.open( 'POST', "/survey/add_survey_in_list/" + form_post.getAttribute("data-pk") + "/", true );
  link_.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

  link_.onreadystatechange = function () {
  if ( this.readyState == 4 && this.status == 200 ) {
    elem = link_.responseText;
    _new = document.createElement("div");
    _new.innerHTML = elem;
    if (document.querySelector(".attach_block")){
      document.body.querySelector(".attach_block").append(_new.querySelector(".load_pag"));
      add_file_attach();
      is_full_attach();
    } else if (document.querySelector(".message_attach_block")){
      document.body.querySelector(".message_attach_block").append(_new.querySelector(".load_pag"));
      add_file_attach();
      is_full_attach();
    }
    else {
        container = document.body.querySelector(".is_paginate");
        container.insertAdjacentHTML('afterBegin', _new.innerHTML);
        container.querySelector(".items_empty") ? container.querySelector(".items_empty").style.display = "none" : null;
  };
  close_work_fullscreen();
  toast_info("Опрос создан!")
  }};
  link_.send(form_data);
});

on('#ajax', 'click', '.survey_vote', function() {
  _this = this; is_have_vote = false;
  parent = _this.parentElement;
  answers = parent.querySelectorAll(".lite_color");
  if (_this.classList.contains("False")) {
    for (var i = 0; i < answers.length; i++) {
      answers[i].querySelector(".vote_svg").innerHTML = "";
     };
     is_have_vote = true
  } else {
    is_have_vote = true
  };
  if (_this.querySelector(".vote_svg").innerHTML) {
    _this.querySelector(".vote_svg").innerHTML = ''
    for (var i = 0; i < answers.length; i++) {
      if (answers[i].querySelector(".vote_svg").innerHTML) {
        is_have_vote = true
      }
     };
  } else {
    _this.querySelector(".vote_svg").innerHTML = '<input type="hidden" name="votes" value="' + _this.getAttribute("data-pk") + '"><svg fill="currentColor" style="width:15px;height:15px;" class="svg_default" viewBox="0 0 24 24"><path fill="none" d="M0 0h24v24H0z"></path><path d="M9 16.2L4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"></path></svg>'
  };
  if (is_have_vote) {
    footer = parent.nextElementSibling
    footer.querySelector(".votes_remove").classList.remove("hidden");
    footer.querySelector(".float-right").classList.remove("hidden")
  }
});

on('#ajax', 'click', '.votes_remove', function() {
  _this = this;
  block = _this.previousElementSibling;
  answers = block.querySelectorAll(".lite_color");
  for (var i = 0; i < answers.length; i++) {
    answers[i].querySelector(".vote_svg").innerHTML = "";
  };
  _this.classList.remove("hidden");
  _this.classList.nextElementSibling.remove("hidden");
});
