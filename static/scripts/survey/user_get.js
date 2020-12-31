on('#ajax', 'click', '.u_add_survey', function() {
  loader = document.getElementById("create_loader");
  open_fullscreen('/survey/user_progs/add/', loader);
});

on('#ajax', 'click', '#need_time_end', function() {
  this.parentElement.parentElement.nextElementSibling.classList.toggle("hide")
});

on('#ajax', 'click', '.remove_answer', function() {
  this.remove()
});
on('#ajax', 'click', '.add_answer', function() {
  container = this.parentElement.parentElement
  answers = container.querySelectorAll(".answer");
  answers.length > 9 ? toast_error("Допустимо не больше 10 вариантов!") :
  (div = document.createElement("div"), div.classList.add("form-group"),
  div.innerHTML = '<div class="input-group pointer remove_answer"><input type="text" name="answers" placeholder="Вариант ответа" class="form-control answer"><div class="input-group-append"><span class="input-group-text custom_color">x</span></div></div>',
  container.append(div));
});
