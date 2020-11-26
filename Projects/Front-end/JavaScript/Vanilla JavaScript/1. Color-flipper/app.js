const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];
const btn = document.getElementById('btn')
const color = document.querySelector(".color-name")

btn.addEventListener('click', function() {
// get random number between 0-3 (cause the the list contains 4 values)
 const randomNumber = getRandomNumber();
 document.body.style.backgroundColor = colors[randomNumber]; // choose color from the list and display it as the background color 
  color.textContent = colors[randomNumber]; // display the current background color as text
})

// Function that generates random numbers
function getRandomNumber() {
    return Math.floor(Math.random() * colors.length);
}