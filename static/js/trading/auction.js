var noob = undefined;
$(document).ready(function() {
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
});