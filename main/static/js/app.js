
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

const modalAgrad = document.getElementById('modal-agradecimento')
modalAgrad.addEventListener('click', function (e){
    if (e.target.id == 'modal-agradecimento' || e.target.className == 'fechar' ) {
        modalAgrad.classList.remove('mostrar')
    }
});



// const btAgrad = document.querySelector('.bt-enviar');
// btAgrad.addEventListener('click', function () {
//     iniciaModal('modal-agradecimento');
//     })




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

