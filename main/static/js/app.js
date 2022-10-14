
function iniciaModal(modalID) {
    const modal = document.getElementById(modalID)
    if (modal) {
        modal.classList.add('mostrar');
        modal.addEventListener('click', function (e) {
            if (e.target.id == modalID || e.target.className == 'fechar' ) {
                modal.classList.remove('mostrar')
            }
        });
    }
}

// || e.target.className == 'bt-enviar'
const btCot = document.querySelector('.botao')
btCot.addEventListener('click', function () {
    iniciaModal('modal-contato');
});

const form = document.getElementById('modal-form')
form.addEventListener('submit', function () {
    const modal = document.getElementById('modal-contato')
    modal.classList.remove('mostrar');
    iniciaModal('modal-agradecimento');
});


// const btAgrad = document.querySelector('.bt-enviar');
// btAgrad.addEventListener('click', function () {
//     iniciaModal('modal-agradecimento');
//     })






//scroll aparencendo
const elementos = document.querySelectorAll('[data-animate]');

//scrollTop


function mascara(telefone){ 
    if(telefone.value.length == 0)
        telefone.value = '(' + telefone.value; //quando começamos a digitar, o script irá inserir um parênteses no começo do campo.
    if(telefone.value.length == 3)
        telefone.value = telefone.value + ') '; //quando o campo já tiver 3 caracteres (um parênteses e 2 números) o script irá inserir mais um parênteses, fechando assim o código de área.

    if(telefone.value.length == 10)
        telefone.value = telefone.value + '-'; //quando o campo já tiver 8 caracteres, o script irá inserir um tracinho, para melhor visualização do telefone.
    if(telefone.value.length == 15)
        telefone.value
}

