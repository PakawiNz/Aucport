$(function () {
    $('#register').click(function(){
        var mainform = $('#mainform')[0];
        var register = $('#register');
        register.parent().prepend('<img class="loading" src="/static/img/loading.gif"></img>');
        doajax({
            url: mainform.action,
            type: mainform.method,
            dataType: 'json',
            data: $('#mainform').serialize(),
            success: function(result) {
                if (result.success){
                    var input = $("<input>").attr("type", "hidden").attr("name", "isSubmit").val("true");
                    $('#mainform').append($(input));
                    mainform.submit();
                }else {
                    $('.descbox').remove();
                    $('.has-error').removeClass('has-error');
                    for (var target in result.errorList){
                        var input = $('#' + target);
                        var inputblock = input.closest('.detail > .input-group');
                        inputblock.addClass('has-error');
                        var desc = '<div class="input-group-addon descbox">' + result.errorList[target] + '</div>';
                        inputblock.append(desc);
                    }
                }
            },
            complete : function(){
                $('.loading').fadeOut();            
            }
        });
    });

    $('a.openeditlink').click(function(event){
        alert(event.target.val);
        url = $("#e_product").val();
        $.form(url, { product: id }, 'POST').submit();
    });

    $('#expired').datetimepicker({
        minDate:  new Date(),
    });

    getOldpicture = function(num){
        var pictures = $('.oldpicture');
        if (pictures[num-1] != undefined)
            return ["<img src='" + pictures[num-1].src + "' class='file-preview-image'>"];
        else 
            return undefined;
    }

    $("#picture1").fileinput({
        initialPreview: getOldpicture(1),
        overwriteInitial: true,
        previewFileType: "picture",
        allowedFileExtensions: ["jpg"],
        browseClass: "btn btn-default",
    });
    $("#picture2").fileinput({
        initialPreview: getOldpicture(2),
        overwriteInitial: true,
        previewFileType: "picture",
        allowedFileExtensions: ["jpg"],
        browseClass: "btn btn-default",
    });
    $("#picture3").fileinput({
        initialPreview: getOldpicture(3),
        overwriteInitial: true,
        previewFileType: "picture",
        allowedFileExtensions: ["jpg"],
        browseClass: "btn btn-default",
    });
    $("#picture4").fileinput({
        initialPreview: getOldpicture(4),
        overwriteInitial: true,
        previewFileType: "picture",
        allowedFileExtensions: ["jpg"],
        browseClass: "btn btn-default",
    });
    $("#picture5").fileinput({
        initialPreview: getOldpicture(5),
        overwriteInitial: true,
        previewFileType: "picture",
        allowedFileExtensions: ["jpg"],
        browseClass: "btn btn-default",
    });
});