// classList - shows/gets all classes
// contains - checks classList for specific class
// add - add class
// remove - remove class
// toggle - toggles class

const navToggle = document.querySelector('.nav-toggle')
const links = document.querySelector('.links')


// when click on the nav bar -> show/hide nav buttons
navToggle.addEventListener('click', function () {
    // console.log(links.classList) - print links connected classes
    // console.log(links.classList.contains('random')); - print false
    // console.log(links.classList.contains('show-links')); - print true

    // // if the nav bar open press to close him
    // if (links.classList.contains('show-links')) {
    //     links.classList.remove('show-links')
    // }

    // // if the nav bar close press to open him
    // else {
    //     links.classList.add("show-links")
    // }

    // press to open and close the nav bar
    // if the nav bar open this function will remove the class "show-links" from the html
    // if the nav bar closed this function will add the class "show-links" to the html
    links.classList.toggle("show-links")

})
