function description(task) {
	$(document).ready(function(){
		$('#'+task+' .desc').slideDown();
		$('#'+task+' .desc .description').fadeIn();
	});
}


function submit(task) {
	$(document).ready(function(){
		$('#'+task+' .apply').slideDown();
		$('#'+task+' .apply .appy').fadeIn();
	});
}

function closea(task) {
	$(document).ready(function(){
		$('#'+task+' .desc').slideUp();
		$('#'+task+' .desc .description').fadeOut();
	});
}

function closeb(task) {
	$(document).ready(function(){
		$('#'+task+' .apply').slideUp();
		$('#'+task+' .apply .appy').fadeOut();
	});
}

$('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
        || location.hostname == this.hostname) {

        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
           if (target.length) {
             $('html,body').animate({
                 scrollTop: target.offset().top
            }, 1000);
            return false;
        }
    }
});

// function countdown(task) {
// 	var dead = "{{task.submission_deadline}}";
// 	console.log(dead);
// 	var countDownDate = new Date(dead + ', 2018 13:00:00').getTime();
//
// 	var x = setInterval(function() {
// 		var now = new Date().getTime();
// 		var distance = countDownDate - now;
//
// 		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
// 		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
// 		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
// 		var seconds = Math.floor((distance % (1000 * 60)) / 1000);
//
// 		document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
// 		+ minutes + "m " + seconds + "s ";
//
// 		if (distance < 0) {
// 			clearInterval(x);
// 			document.getElementById("countdown").innerHTML = "EXPIRED";
// 	 }
// 	}, 1000);
// }
