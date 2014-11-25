var doajax = function(){};
$(function(){
    //Handles menu drop down
    $('.dropdown-menu').find('form').click(function (e) {
        e.stopPropagation();
    });

    var url = document.URL;
    var page = url.split('/')[4];
    if (page == "register"){
    	$('#nav4').addClass('active');
    }else if (page == "register"){
    	$('#nav4').addClass('active');
    }

    var csrf = $('meta[name="csrf"]').attr('content')
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrf);
        }
    });

    doajax = function(data){
        data.dataType = 'json';
        data.type = "POST";
        if (!data.sendform) {
            data.data = JSON.stringify(data.data);
            data.contentType = "application/json; charset=utf-8";
        }
        $.ajax(data);
    }

    $('[data-toggle="tooltip"]').tooltip();
});