
const elementos = document.querySelectorAll('[data-anime]');

function animeScroll(){
    const windowTop = window.pageYOffset + ((window.innerHeight * 3) / 4);
    elementos.forEach(function(e){
        if ((windowTop) > e.offsetTop){
            e.classList.add('animate')
        } else {
            e.classList.remove('animate')
        }
    })
}

animeScroll();

if(elementos.length) {
    window.addEventListener('scroll', function() {
        animeScroll();
    });
}

const menuItems = document.querySelectorAll('.nav-link[href^="#"]');


menuItems.forEach(item => {
    item.addEventListener('click', scrollParaID)
});


function scrollParaID(event){
    event.preventDefault();
    const elemento = event.target
    const id = elemento.getAttribute('href')
    const to = document.querySelector(id).offsetTop;

    window.scroll({
        top: to - 80,
        behavior: 'smooth',
    })

}



let slides = document.querySelectorAll('.slide-container');
let index = 0;

function next(){
    slides[index].classList.remove('active');
    index = (index + 1) % slides.length;
    slides[index].classList.add('active');
}

function prev(){
    slides[index].classList.remove('active');
    index = (index - 1 + slides.length) % slides.length;
    slides[index].classList.add('active');
}


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


function imgPrincipal() {
    var source = document.getElementById("imgPrincipal").src;
    document.getElementById("trocarImg").src=source;
}

function img1() {
    var source = document.getElementById("img1").src;
    document.getElementById("trocarImg").src=source;
}

function img2() {
    var source = document.getElementById("img2").src;
    document.getElementById("trocarImg").src=source;
}

function img3() {
    var source = document.getElementById("img3").src;
    document.getElementById("trocarImg").src=source;
}

function img4() {
    var source = document.getElementById("img4").src;
    document.getElementById("trocarImg").src=source;
}


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


