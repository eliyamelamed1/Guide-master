const toggleBtn = document.querySelector(".sidebar-toggle")
const closeBtn = document.querySelector(".close-btn")
const sidebar = document.querySelector(".sidebar")

// function to open & close side-bar
// if "show-sidebar" is in the html
// it means the side-bar is open
// so to close it you have to remove "show-sidebar"

// the .toggle command is a function that check if a variable contain "value"
// if True it will be removed
// If False it will be added
toggleBtn.addEventListener('click', function () {
    console.log(sidebar.classList)
    // if (sidebar.classList.contains("show-sidebar")) {
    //     sidebar.classList.remove("show-sidebar")
    // }
    // else {
    //     sidebar.classList.add("show-sidebar")
    // }
    
    sidebar.classList.toggle('show-sidebar')
})

closeBtn.addEventListener('click', function () {
    sidebar.classList.remove("show-sidebar")
})