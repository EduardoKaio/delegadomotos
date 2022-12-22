
$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
 });

// function mostrarValor() {
    
//     console.log("clicou")
//     pk = {{ Moto.id }}

//     console.log(pk)
// }

// // Evento que é executado toda vez que uma tecla for pressionada no input
// document.getElementById("id_is_visibility_teste").onclick = function(e) {

//         mostrarValor();
//         e.preventDefault();
// }

// // Evento que é executado ao clicar no botão de enviar
// document.getElementById("submitId").onclick = function(e) {
//     mostrarValor();
//     e.preventDefault();
// }





// let checkboxes = document.querySelectorAll('#id_is_visibility_teste');
// checkboxes.addEventListener('click', function (e){
//     const pk = e.value
//     console.log(pk)
// });

// document.addEventListener('is_visibility', function() {
//     checkboxes.forEach(checkbox => {
//         checkbox.onclick = function() {
//             const pk = checkbox.Moto.id
//             console.log(pk)
//         }
//     });
// });