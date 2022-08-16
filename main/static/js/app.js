//scroll aparencendo
const elementos = document.querySelectorAll('[data-animate]');


//scrollTop
$('nav a').click(function (e) {
    e.preventDefault();
    var id = $(this).attr('href'),
        targetOffset = $(id).offset().top;

    $('html, body').animate({
        scrollTop: targetOffset - 94
    }, 100);
});


