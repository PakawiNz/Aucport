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
				window.clearInterval(timerId);
				return;
			}
			document.getElementById(major).innerHTML = ts.hours + ':' + ts.minutes;
			document.getElementById(minor).innerHTML = ts.seconds;
		},countdown.HOURS|countdown.MINUTES|countdown.SECONDS);
	});

	var pids = [];
	$(".auction").map(function(){
	  pids.push($(this).attr('pid'));
	});
	function refreshPrice_success(aucid,product){
		var logo = "";
		if (product.king) logo = "<span class='fa fa-flag' style='color:rgba(255, 0, 97, 1);'></span> ";
		var newPrice = parseFloat(product.maxprice).toFixed(1);
		var context = logo + newPrice + ' ';
		var price = $('#price'+ aucid);

		if (product.isExpired){
			var endTime = $('#endTime' + aucid);
			endTime.fadeOut(function(){
				$('#endMajor' + aucid).addClass("clock").removeClass("day")
				if (product.king) {
					$('#endMajor' + aucid).html('You');
					$('#endMinor' + aucid).html('Win');
           			price.tooltip('show');
               		setTimeout(function () {
	           			price.tooltip('hide');
				    }, 4000);
				    price.parent().attr('href',price.parent().attr('ref'));
				    price.parent().parent().addClass('hoverable')
				}else {
					$('#endMajor' + aucid).html('Time');
					$('#endMinor' + aucid).html('up');
				}
				$('#endTime' + aucid).css('background-color',"black");
				endTime.fadeIn(function(){
					$('#auctioner' + aucid).slideUp();
				});
			});
			var index = pids.indexOf(aucid);
			if (index > -1) pids[index] = 0;
		}

		$('#current' + aucid).attr('placeholder',product.curprice);
		if (price.val() == newPrice) return; 
		price.val(newPrice);
		$('#price'+ aucid).fadeOut(function(){
			$('#price'+ aucid).html(context);
			$('#price'+ aucid).fadeIn();
		});
	}
	function refreshPrice(pid){
		var data = {'pids':pids};
		if (pid) {
			data.pids = [pid];
		}
		doajax({
			url: '/trading/getupdated/',
            data: data,
            success: function(result) {
            	for (var pid in result.products){
            		refreshPrice_success(pid,result.products[pid]);
            	}
            },
		});
	}

	refreshPrice();
	setInterval( function(){
		refreshPrice();
	}, 5000 );

	$('.toggle-btn').click(function(event){
		var url = $("#main").attr("action");
		var caller = $(this);
		var auction = caller.data("auction");
		var target = caller.data("target");
		var input = $('#'+target);
		var name = input.attr("name");

		var data = {};
		data[name] = input.val() == 0;
		data['auction'] = auction;

		var spinning = caller.children('.fa').first();

		caller.removeClass('btn-info btn-default');
		spinning.removeClass('fa-spin');

        doajax({
            url: url,
            type: "POST",
            dataType: 'json',
            data: data,
            success: function(result) {
                if (result.success){
               		if (data[name]) {
	               		input.val(1);
               			caller.addClass('btn-info')
						spinning.addClass('fa-spin');
               		}else {
	               		input.val(0);
               			caller.addClass('btn-default')
               		}
                }
           		refreshPrice();
            },
        });
	});

	$('.update-btn').click(function(event){
		var url = $("#main").attr("action");
		var caller = $(this);
		var auction = caller.data("auction");
		var target = caller.data("target");
		var input = $('#'+target);
		var name = input.attr("name");

		var data = {};
		data[name] = input.val();
		alert(data[name]);
		data['auction'] = auction;

        caller.prepend('<span class="loading fa fa-refresh fa-spin" style="display:none;"></span>');
        var loading = caller.children('.loading').first();
        loading.fadeIn();
		doajax({
            url: url,
            type: "POST",
            dataType: 'json',
            data: data,
            success: function(result) {
               if (result.unwatched != undefined){
               		$('#auction' + auction).fadeOut();
               		$('#auctioner' + auction).fadeOut();
               }else if (result.success){
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
                loading.fadeOut(function(){
                	loading.remove();
                });
            },
        });
	});
});