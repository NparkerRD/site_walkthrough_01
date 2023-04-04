const btnNewCompany = document.querySelector("#btn--newCompany");
const cancelBtn = document.querySelector('#btnCancel');
const modalNewCompany = document.querySelector('#modal--newCompany')
const btnNewLocation = document.querySelector('#btn--newLocation')
const modalNewLocation = document.querySelector('#modal--newLocation')

// Open New Company modal
// Turn into function?
if (btnNewCompany) {
    btnNewCompany.addEventListener('click', (e) => {
        e.preventDefault();
        modalNewCompany.classList.remove('hidden');
    })
} else {
    console.log("New company button does NOT exist");
}

// Close Modal Logic - Universal
cancelBtn.addEventListener('click', (e) => {
    e.preventDefault();
    cancelBtn.closest('.modal').classList.add('hidden');
})

// Open New Location modal
if (btnNewLocation) {
    btnNewLocation.addEventListener('click', (e) => {
        e.preventDefault();
        modalNewLocation.classList.remove('hidden');
    })
} else {
    console.log("New Location button does NOT exist");
}

// Functions
