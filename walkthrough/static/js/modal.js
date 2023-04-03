const openBtn = document.querySelector("#btnOpenModal");
const cancelBtn = document.querySelector('#btnCancel');
const modal = document.querySelector('.modal')

// Open Modal Logic - (may not be needed)
openBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.remove('hidden');
})

// Close Modal Logic
cancelBtn.addEventListener('click', (e) => {
    e.preventDefault();
    modal.classList.add('hidden')
})
// Modal from 850 Consulting
// const modalEl = document.getElementById("modal");
// const myModal = document.querySelector('dialog');
// const requestConsultButtons = Array.from(document.getElementsByClassName("requestConsultBtn"));
// const cancelBtn = document.getElementById("cancelBtn");

// requestConsultButtons.forEach(btn => {
//     btn.addEventListener('click', function(){
//         modalEl.classList.remove('hidden');
//     });
// });

// cancelBtn.addEventListener("click", function (){
//     modalEl.classList.add('hidden');
// });