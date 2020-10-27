const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
// #f15025 example of hex color
const btn = document.getElementById('btn') // Acsessing html id value
const color = document.querySelector('.color-name')

btn.addEventListener('click', function() {
let hexColor = '#';
for (let i = 0; i<6; i++) {
 hexColor += hex[getRandomNumber()] 
}
color.textContent = hexColor;  // Display the hexColor as text
document.body.style.background = hexColor // Display the background color as the hexColor
})

// Function that generates random numbers 
function getRandomNumber() {
    return Math.floor(Math.random() * hex.length)
}