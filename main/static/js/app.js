
function iniciaModal(modalID) {
    const modal = document.getElementById(modalID)
    if (modal) {
        modal.classList.add('mostrar');
        modal.addEventListener('click', function (e) {
            if (e.target.id == modalID || e.target.className == 'fechar' || e.target.className == 'bt-enviar') {
                modal.classList.remove('mostrar')
            }
        });
    }
}

const btCot = document.querySelector('.botao')
btCot.addEventListener('click', function () {
    iniciaModal('modal-contato');
});


const btAgrad = document.querySelector('.bt-enviar')
btAgrad.addEventListener('click', function () {
    iniciaModal('modal-agradecimento');
});




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


