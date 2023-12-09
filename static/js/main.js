// -----------------------login modal----------------------------------------------------

document.getElementById('openlogin').addEventListener("click", function () {
    document.getElementById('modellogin').classList.add('open')
    document.getElementById('modelsignup').classList.remove('open')
});

document.getElementById('close-login-model').addEventListener("click", function () {
    document.getElementById('modellogin').classList.remove('open')
});

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.getElementById('modellogin').classList.remove('open')
    }
});
document.querySelector("#modellogin .model__box").addEventListener("click", event => {
    event._isClickWithInModal = true
})
document.getElementById("modellogin").addEventListener("click", event => {
        if (event._isClickWithInModal) return;
        event.currentTarget.classList.remove('open')
    }
)
//-------------------------------------------------------------------------------------------------------------------------


// -----------------------signup modal--------------------------------------------------

document.getElementById('opensignup').addEventListener('click', function () {
    document.getElementById('modelsignup').classList.add('open')
    document.getElementById('modellogin').classList.remove('open')
})
document.getElementById('close-signup-model').addEventListener("click", function () {
    document.getElementById('modelsignup').classList.remove('open')
})
document.getElementById('openloginagain').addEventListener("click", function () {
    document.getElementById('modellogin').classList.add('open')
    document.getElementById('modelsignup').classList.remove('open')
});
window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.getElementById('modelsignup').classList.remove('open')
    }
});

document.querySelector("#modelsignup .model__box").addEventListener("click", event => {
    event._isClickWithInModal = true
})
document.getElementById("modelsignup").addEventListener("click", event => {
        if (event._isClickWithInModal) return;
        event.currentTarget.classList.remove('open')
    }
)

//---------------------------------------------------------------------------------------------------------------------------


// -----------------------category modal--------------------------------------------------------

document.getElementById('opencategories').addEventListener("click", function () {
    document.getElementById('modalcategory').classList.add('open')
})
document.getElementById('close-category-modal').addEventListener("click", function () {
    document.getElementById('modalcategory').classList.remove('open')
})


document.getElementById('openloginagaininmenu').addEventListener("click", function () {
    document.getElementById('modellogin').classList.add('open')
    document.getElementById('modalcategory').classList.remove('open')
});

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.getElementById('modalcategory').classList.remove('open')
    }
});


document.querySelector("#modalcategory .modal__category_box").addEventListener("click", event => {
    event._isClickWithInModal = true
})
document.getElementById("modalcategory").addEventListener("click", event => {
        if (event._isClickWithInModal) return;
        event.currentTarget.classList.remove('open')
    }
)


//---------------------------------------------------------------------------------------------------------------------------


