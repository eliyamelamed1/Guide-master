// select modal-btn,modal-overlay,close-btn
// listen for click events on modal-btn and close-btn
// when user clicks modal-btn add .open-modal to modal-overlay
// when user clicks close-btn remove .open-modal from modal-overlay

// Declaring open & close buttons
const openBtn = document.querySelector(".modal-btn") 
const closeBtn = document.querySelector(".close-btn")

// "modal-overlay" is a css class that makes the button do nothing
// when "open-modal" is added to that class he is overwriting her to make the button work 
const modal = document.querySelector(".modal-overlay")



openBtn.addEventListener('click', function () {

    modal.classList.add("open-modal")
})

closeBtn.addEventListener('click', function () {

    modal.classList.remove("open-modal")
})

