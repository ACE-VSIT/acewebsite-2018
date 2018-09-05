(function($) {
    'use strict';
    $(function() {
<<<<<<< HEAD
        $('.cancel-link').click(function(e) {
            e.preventDefault();
            window.history.back();
=======
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back();  // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
>>>>>>> b11e8b8b121afc12bdc9fc35b3208d96b477c51c
        });
    });
})(django.jQuery);
