$(document).ready(function(){
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
});