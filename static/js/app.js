
// Full  Page Search Activation

$(function () {
    $('a[href="#full-page-search"]').on('click', function(event) {
        event.preventDefault();
        $('#full-page-search').addClass('open');
        $('#full-page-search > form > input[type="search"]').focus();
    });

    $('#full-page-search, #full-page-search button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
            $(this).removeClass('open');
        }
    });
});

 


