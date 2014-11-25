
function pay (e) {
	if ($('creditcard').text.length != 16) {
		return false
	}
	 $( "#dialog-confirm" ).dialog({
	resizable: false,
	// height:140,
	modal: true,
	buttons: {
	"Delete all items": function() {
	$( this ).dialog( "close" );
	},
	Cancel: function() {
	$( this ).dialog( "close" );
	}
	}
	});
}

$(document).ready(function () {
  $("#creditcard").keypress(function (e) {
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        return false;
    }
   });
});
