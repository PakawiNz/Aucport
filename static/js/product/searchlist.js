$(function () {
    $('a.openeditlink').click(function(event){
        var id = event.target.name;
        var form = $("#openeditform");
        form.append("<input type='hidden' name='product' value='" + id + "' />");
        form.submit();
    });
});