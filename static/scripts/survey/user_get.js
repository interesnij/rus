
on('#ajax', 'click', '.load_profile_survey_list', function() {
  profile_list_block_load(this, ".load_block", "/survey_list/", "load_profile_survey_list");
});

on('#ajax', 'click', '.load_attach_survey_list', function() {
  profile_list_block_attach(this, ".load_block", "/u_survey_list_load/", "load_attach_survey_list");
});

on('#ajax', 'click', '.u_add_survey', function() {
  create_fullscreen('/survey/user_progs/add/', "worker_fullscreen");
});

on('#ajax', 'click', '#need_time_end', function() {
  this.parentElement.parentElement.nextElementSibling.classList.toggle("hide")
});

on('#ajax', 'click', '.remove_answer', function() {
  this.parentElement.parentElement.parentElement.remove()
});
on('#ajax', 'click', '.add_answer', function() {
  container = this.parentElement.parentElement.parentElement.parentElement
  answers = container.querySelectorAll(".answer");
  answers.length > 9 ? toast_error("Допустимо не больше 10 вариантов!") :
  (div = document.createElement("div"), div.classList.add("form-group"),
  div.innerHTML = '<div class="input-group"><input type="text" name="answers" placeholder="Вариант ответа" class="form-control answer"><div class="input-group-append"><span class="input-group-text custom_color pointer remove_answer">x</span></div></div>',
  container.append(div));
});
