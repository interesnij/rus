

function getCookie(e){var t=null;if(document.cookie&&""!=document.cookie)for(var o=document.cookie.split(";"),n=0;n<o.length;n++){var r=jQuery.trim(o[n]);if(r.substring(0,e.length+1)==e+"="){t=decodeURIComponent(r.substring(e.length+1));break}}return t}var csrftoken=getCookie("csrftoken");function csrfSafeMethod(e){return/^(GET|HEAD|OPTIONS|TRACE)$/.test(e)}function sameOrigin(e){var t="//"+document.location.host,o=document.location.protocol+t;return e==o||e.slice(0,o.length+1)==o+"/"||e==t||e.slice(0,t.length+1)==t+"/"||!/^(\/\/|http:|https:).*/.test(e)}$.ajaxSetup({beforeSend:function(e,t){!csrfSafeMethod(t.type)&&sameOrigin(t.url)&&e.setRequestHeader("X-CSRFToken",csrftoken)}});
