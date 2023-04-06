'use strict';

const btnNewCompany = document.querySelector("#btn--newCompany");
const btnNewLocation = document.querySelector('#btn--newLocation');

const modalNewCompany = document.querySelector('#modal--newCompany');
const modalNewLocation = document.querySelector('#modal--newLocation');

// Get a list of delete buttons, then open the modal with the matching id
const btnsDelCompany = document.querySelectorAll('.btn--delCompany');
const btnsDelLocation = document.querySelectorAll('.btn--delLocation');

// Get a list of cancel buttons, then close nearest modal
const btnsCancel = document.querySelectorAll('.btn--cancel');

// Functions

// Close open modals
const closeOpenModals = function() {
    const openModals = document.querySelectorAll('.modal--open');
    openModals.forEach(modal => {
        modal.classList.add('hidden');
        modal.classList.remove('modal--open');
    })
};

const openModal = function(modal){
    modal.classList.remove('hidden');
    modal.classList.add('modal--open');
};

// Check if a modal button exists, then add an event listener
const checkButtonExists = function(btn, m) {
    if (btn) {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            // 1) Close all other modals
            closeOpenModals();

            // 2) Display modal
            openModal(m);
        });
    }
};

// Opening modals for deleteing elements/records
const openDeletionConfirmation = function(btns) {
    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            // 1) Close any open modals
            closeOpenModals()

            // 2) Display modal
            const modalConfirmDeletion = document.querySelector(btn.dataset['target']);
            openModal(modalConfirmDeletion);
        })
    })
}

// Closing modals
const closeModal = function(btns){
    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            btn.closest('.modal').classList.add('hidden');
            btn.closest('.modal').classList.remove('modal--open')
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

// Dismissing flashed messages
const btnsDismiss = document.querySelectorAll('.dismiss-msg');
btnsDismiss.forEach(btn => {
    btn.addEventListener('click', (e) => {
        btn.parentElement.remove();
    });
});

/*
ADDRESS LATER:
    * Sort tables by columns

*/