'use strict';

const cancelBtn = document.querySelector('#btnCancel');
const btnNewCompany = document.querySelector("#btn--newCompany");
const btnNewLocation = document.querySelector('#btn--newLocation');
const btnDelCompany = document.querySelector('#btn--delCompany');
const btnDelLocation = document.querySelector('#btn--delLocation');

const modalNewCompany = document.querySelector('#modal--newCompany');
const modalNewLocation = document.querySelector('#modal--newLocation');

// Get a list of delete buttons, then open the modal with the matching id
const btnsDelCompany = document.querySelectorAll('.btn--delCompany');
const btnsDelLocation = document.querySelectorAll('.btn--delLocation');

// Get a list of cancel buttons, then close nearest modal
const btnsCancel = document.querySelectorAll('.btn--cancel');

// Functions
// Check if a modal button exists, then add an event listener
const checkButtonExists = function(btn, m) {
    if (btn) {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            m.classList.remove('hidden');
        })
    }
}

// Opening modals for deleteing elements/records
const openDeletionConfirmation = function(btns) {
    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const modalConfirmDeletion = document.querySelector(btn.dataset['target']);
            modalConfirmDeletion.classList.remove('hidden');
        })
    })
}

// Closing modals
const closeModal = function(btns){
    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            btn.closest('.modal').classList.add('hidden');
        })
    })
}

// Open New Company modal
checkButtonExists(btnNewCompany, modalNewCompany);

// Open New Location modal
checkButtonExists(btnNewLocation, modalNewLocation);

// Open Delete Company modal
openDeletionConfirmation(btnsDelCompany)

// Open Delete Location modal
openDeletionConfirmation(btnsDelLocation)

// Close Modal Logic - Universal
closeModal(btnsCancel)



/*
ADDRESS LATER:
    * Close other modals when new one is opened
    * Sort tables by columns
    * Create logic for dismissing flashed message

*/