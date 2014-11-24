var csrf = "";
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

    csrf = $('meta[name="csrf"]').attr('content')

    doajax = function(data){
        if (data.type.toUpperCase() == 'POST') {
            if (data.data) data.data.csrfmiddlewaretoken = csrf;
            else data.data = {'csrfmiddlewaretoken':csrf,}
        }
        $.ajax(data);
    }

    $('[data-toggle="tooltip"]').tooltip();
});