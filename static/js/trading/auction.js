$(function() {
	auctions.forEach(function(auction){
		var isCounting = false;
		var timeblock = 'endTime' + auction.index;
		var major = 'endMajor' + auction.index;
		var minor = 'endMinor' + auction.index;
		var timerId = countdown(auction.enddate,function(ts) {
			if (ts.hours >= 24) return;
			if (!isCounting){
				isCounting = true;
				document.getElementById(major).className = "clock";
			}
			if (ts.start <= ts.end) {
				document.getElementById(timeblock).style.backgroundColor="black";
				document.getElementById(major).innerHTML = 'Time';
				document.getElementById(minor).innerHTML = 'up';
				window.clearInterval(timerId);
				return;
			}
			document.getElementById(major).innerHTML = ts.hours + ':' + ts.minutes;
			document.getElementById(minor).innerHTML = ts.seconds;
		},countdown.HOURS|countdown.MINUTES|countdown.SECONDS);
	});

	var pids = $(".price").attr("pid");
	function refreshPrice(pid){
		var data = {'pids':pids};
		if (pid) {
			data.pids = [pid];
		}
		doajax({
			url: '/trading/getupdated/',
            type: "POST",
            dataType: 'json',
            data: data,
            success: function(result) {
            	var products = result.products;
            	for (var pid in products){
            		var logo = "";
            		if (products[pid].king) logo = "<span class='fa fa-flag'></span> ";
            		var context = logo + products[pid].maxprice;

            		var price = $('#price'+ pid);
            		if (price.val() == products[pid].maxprice) return; 
            		price.val(products[pid].maxprice);
	            	$('#price'+ pid).fadeOut(function(){
		            	$('#price'+ pid).html(context);
	            		$('#price'+ pid).fadeIn();
	            	});
            	}
            },
		});
	}

	setInterval( function(){
		refreshPrice();
	}, 5000 );

	$('button.update-btn').click(function(event){
		var url = $("#main").attr("action");
		var caller = $(this);
		var auction = caller.data("auction");
		var target = caller.data("target");
		var input = $('#'+target);
		var name = input.attr("name");

		var data = {};
		data[name] = input.val();
		data['auction'] = auction;

        caller.prepend('<img class="loading" src="/static/img/loading.gif"></img>');
		doajax({
            url: url,
            type: "POST",
            dataType: 'json',
            data: data,
            success: function(result) {
               if (result.success){
               		input.val("");
               		input.attr("placeholder",result.newval);
               }else {
           			input.tooltip({
           				'template':'<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner btn-danger"></div></div>',
           				'trigger':'manual',
           				'placement':'bottom',
           				'title':result.error,
           			});
           			input.tooltip('show');
               		setTimeout(function () {
	           			input.tooltip('hide');
				    }, 2000);
               }
           		refreshPrice();
            },
            complete : function(){
                $('.loading').fadeOut();
            },
        });
	});
});