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