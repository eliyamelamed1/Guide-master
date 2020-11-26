// const value = document.getElementById('value')
// =
// const value = document.querySelector('#value')

// The forEach() method executes a provided function once for each array element.



// set initial count
let count = 0;

// select value and buttons
const value = document.querySelector('#value')

// All '.btn' classes stored in btns array
const btns = document.querySelectorAll('.btn') 


btns.forEach(function (btn) 
{
    btn.addEventListener('click', function(example)
    {
        const styles = example.currentTarget.classList
        if (styles.contains('decrease'))
        {
            count--;
        }
        else if (styles.contains("increase")) {
            count++; 
        }
        else {
            count = 0;
        }
        if (count > 0) {
            value.style.color = 'green';
        }
        else if (count < 0) {
            value.style.color = 'red';
        }
        else {
            value.style.color = 'black';
        }
        
        value.textContent = count;
    })
});
