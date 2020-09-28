// Declaring ac button
const AllClear = document.querySelector(".two-squares")
const pre = document.querySelector(".pre-num")
const current = document.querySelector(".current-num")
const num1 = document.querySelector(".num1")
const num2 = document.querySelector(".num2")
const num3 = document.querySelector(".num3")
const num4 = document.querySelector(".num4")
const num5 = document.querySelector(".num5")
const num6 = document.querySelector(".num6")
const num7 = document.querySelector(".num7")
const num8 = document.querySelector(".num8")
const num9 = document.querySelector(".num9")
const num0 = document.querySelector(".num0")
const dot = document.querySelector(".dot")

const power = document.querySelector(".power")
const plus = document.querySelector(".plus")
const minus = document.querySelector(".minus")
const del = document.querySelector(".Delete")
const fractional = document.querySelector(".fractional")
const answer = document.querySelector(".answer")


const btns = document.querySelectorAll('.btn') 
var operations = 0; // two operations in row are not allowed
const a = 1  
btns.forEach(function (btn) 
{   

    btn.addEventListener('click', function(example)
    {   
        const styles = example.currentTarget.classList
        if (a == 1) 
        {
            // Buttons of numbers
            if (styles.contains('num0'))
            {
                current.innerText += 0 
            }
            if (styles.contains('num1'))
            {
                current.innerText += 1 
            }
            
            if (styles.contains('num2'))
            {
                current.innerText += 2 
            }
            
            if (styles.contains('num3'))
            {
                current.innerText += 3 
            }
            
            if (styles.contains('num4'))
            {
                current.innerText += 4 
            }
            
            if (styles.contains('num5'))
            {
                current.innerText += 5 
            }
            
            if (styles.contains('num6'))
            {
                current.innerText += 6 
            }
            
            if (styles.contains('num7'))
            {
                current.innerText += 7 
            }
            
            if (styles.contains('num8'))
            {
                current.innerText += 8
            }
            
            if (styles.contains('num9'))
            {
                current.innerText += 9 
            }
            if (styles.contains('two-squares')) 
            {
                current.innerText = ""
                pre.innerText = ""
            }
            if (styles.contains('Delete')) 
            {
            current.innerText = current.innerText.slice(0,-1)
            }

            if (styles.contains('answer')) 
            {
            current.innerText = eval(current.innerText)
            }

            operations = 0;

        }

        if (operations == 0) 
        {
        
            // Buttons of operations
            if (styles.contains('power')) 
            {
              current.innerText += "*"
            }

            if (styles.contains('plus')) 
            {
                current.innerText += "+" 
            }

            if (styles.contains('minus')) 
            {
                current.innerText += "-" 
            }

            if (styles.contains('fractional')) 
            {
                current.innerText += "/" 

            }
            if (styles.contains('dot'))
            {
                current.innerText += ".";            
                
            }
            
            operations = 1
        }
          
    })

});

