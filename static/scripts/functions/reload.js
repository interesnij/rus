function create_reload_page(form, post_link, history_link) {
	form_data = new FormData(form);
  var ajax_link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
    ajax_link.open( 'POST', post_link, true );
    ajax_link.onreadystatechange = function () {
      if ( this.readyState == 4 && this.status == 200 ) {
          elem_ = document.createElement('span');
          elem_.innerHTML = ajax_link.responseText;
          ajax = elem_.querySelector("#reload_block");
          rtr = document.getElementById('ajax');
          rtr.innerHTML = ajax.innerHTML;
          pk = rtr.querySelector(".pk_saver").getAttribute("data-pk");
          window.scrollTo(0,0);
          document.title = elem_.querySelector('title').innerHTML;
          if_list(rtr);
          window.history.pushState(null, "vfgffgfgf", history_link + pk + '/');
      }
    }
    ajax_link.send(form_data);
}

function scrolled(block, link, block_2){
	// скрипты для работы с прокруткой: пагинация, просмотры и т.д.
	onscroll = function(){
		var box = block.querySelector('.last');
		if(box && box.classList.contains("last")){
				inViewport = elementInViewport(box);
				if(inViewport){
					box.classList.remove("last");
					console.log(i + " удалил класс last");
					paginate(block, link, block_2)
		}};
	}
}
page = 2;
loaded = false;
function paginate(block, link, block_2){
	if(block.getElementsByClassName('pag').length === (page-1)*3){
		if (loaded){return};
		var link_3 = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
		link_3.open( 'GET', link + '/?page=' + page++, true );

		link_3.onreadystatechange = function () {
		if ( this.readyState == 4 && this.status == 200 ) {
			var elem = document.createElement('span');
			elem.innerHTML = link_3.responseText;
			if(elem.getElementsByClassName('pag').length < 3){loaded = true; return};
			if (elem.querySelector(block_2)){
				xxx = document.createElement("span");
				xxx.innerHTML = elem.querySelector(block_2).innerHTML;
				block.append(xxx)
			} else {block.append(elem)}
			}
		}
		link_3.send();
	}
}

function create_pagination(block){
	// подключаем подгрузкку списков всех страниц с содержимым. Прозванивать придется все страницы со списками.
	if(block.querySelector('#music_tag_container')){
    music_tag = block.querySelector('#tag_container');
		_link = music_tag.getAttribute("data-link");
		scrolled(music_tag, _link, '#tag_container')
  } else if(block.querySelector('#lenta_load')){
		lenta_load = block.querySelector('#lenta_load');
		_link = lenta_load.getAttribute("data-link");
		scrolled(lenta_load, _link, '#lenta_load');
	} else if(block.querySelector('#music_genre_container')){
		music_genre = block.querySelector('#genre_container');
		_link = music_genre.getAttribute("data-link");
		scrolled(music_genre, _link, '#genre_container');
	}
}
function if_list(block){
  // проверяем, если ли на странице блок с подгрузкой списка. Если есть, грузим список/С пагинацией сразу
  if(block.querySelector('#news_load')){
    news_load = block.querySelector('#news_load');link = news_load.getAttribute("data-link");
    list_load(block.querySelector("#news_load"), link);
  }else if(block.querySelector('#lenta_load')){
    lenta_load = block.querySelector('#lenta_load');
		link = lenta_load.getAttribute("data-link");
    list_load(lenta_load, link);
		scrolled(lenta_load, link, '#lenta_load')

  }else if(block.querySelector('#lenta_community')){
    lenta_community = block.querySelector('#lenta_community');link = lenta_community.getAttribute("data-link");
    list_load(block.querySelector("#lenta_community"), link);
  }else if(block.querySelector('#photo_load')){
    photo_load = block.querySelector('#photo_load');link = photo_load.getAttribute("data-link");
    list_load(block.querySelector("#photo_load"), link);
  }else if(block.querySelector('#album_photo_load')){
    album_photo_load = block.querySelector('#album_photo_load');link = album_photo_load.getAttribute("data-link");
    list_load(block.querySelector("#album_photo_load"), link);
  };
}
if_list(document.getElementById('ajax'));
create_pagination(document.getElementById('ajax'));

function list_load(block,link) {
  // подгрузка списка
  var request = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );request.open( 'GET', link, true );request.onreadystatechange = function () {if ( request.readyState == 4 && request.status == 200 ) {block.innerHTML = request.responseText;}};request.send( null );
}

function ajax_get_reload(url) {
	// перезагрузка основного блока на страницу с указанным url
  var ajax_link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
    ajax_link.open( 'GET', url, true );
    ajax_link.onreadystatechange = function () {
      if ( this.readyState == 4 && this.status == 200 ) {
        elem_ = document.createElement('span');
        elem_.innerHTML = ajax_link.responseText;
        ajax = elem_.querySelector("#reload_block");
        rtr = document.getElementById('ajax');
        rtr.innerHTML = ajax.innerHTML;
        window.scrollTo(0,0);
        title = elem_.querySelector('title').innerHTML;
        window.history.pushState(null, "vfgffgfgf", url);
        document.title = title;
        if_list(rtr);
        load_chart();
				page = 2;
				loaded = false;
				create_pagination(rtr);
      }
    }
    ajax_link.send();
}
