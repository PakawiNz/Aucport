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

    $('#birthdate').datetimepicker({
        pickTime: false,
        maxDate:  new Date(),
        useStrict: true
    });

    $('.button-checkbox').each(function () {

        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color'),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };

        // Event Handlers
        $button.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');

            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Set the button's icon
            $button.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$button.data('state')].icon);

            // Update the button's color
            if (isChecked) {
                $button
                    .removeClass('btn-default')
                    .addClass('btn-' + color + ' active');
            }
            else {
                $button
                    .removeClass('btn-' + color + ' active')
                    .addClass('btn-default');
            }
        }

        // Initialization
        function init() {

            updateDisplay();

            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i>');
            }
        }
        init();
    });

    getOldpicture = function(){
        if ($('#oldpicture')[0])
            return ["<img src='" + $('#oldpicture')[0].src + "' class='file-preview-image'>"];
        else 
            return undefined;
    }

    $("#picture").fileinput({
        initialPreview: getOldpicture(),
        overwriteInitial: true,
        initialCaption: "Old Picture",
        previewFileType: "picture",
        allowedFileExtensions: ["jpg","png"],
        browseClass: "btn btn-default",
    });
});