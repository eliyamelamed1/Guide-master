console.log() // same as print() in python
alert() // creates alert box
  
  
               /* JS on Html file */
  
<p id="demo"></p>

<script>
var carName = "Volvo";
document.getElementById("demo").innerHTML = carName;
</script>

                  /* JS events */
                    
// JS contains many events for many situations
// this time the event used is: onclick
                   
 // Display the date after clicking the button                 
 <button onclick="document.getElementById('demo').innerHTML = Date()">
 The time is?
 </button>
 // or   
 <button onclick="displayDate()">
 The time is?
 </button>           
 
 
 // After clicking the button
 // the button text change to the date
 <button onclick="this.innerHTML = Date()">
 The time is?
 </button>
 
 
               /* Assigning Variables */
                 

// Multiple assignments 
var x // undefined
, number = 10
, string = "Sentence"
, boolean = true
, nothing = Null
, array = ["Mike", "Tom"]
, object = {
 FirstName:"Eliya", 
 LastName: "Melamed"
 };

var a = 16 + 4 + "Volvo" // - - > a = "20Volvo"

var b = "Volvo" + 16 + 4 // - - > b = "Volvo164"


                  /* Arrays */
// Creating a list                   
list = ["Audi", "BMW", "Tesla"] 

// modifying list values
list[0] = "Toyota"                


                    /* Object */
                      
 // Creating Object                     
 var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

// using function in object
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
}; 

// In a function definition, 'this' refers to the "owner" of the function.
// In the example above, this is the person object that "owns" the fullName function.
// In other words, this.firstName means the firstName property of this object.

// Modifying Object attributes
person.age = 10;
// or
person["age"] = 20;

// delete Object attribute 
delete person["age"];

var x = person // now x isn't person's copy. They're the same Object. 


// Accessing Object Methods      
// objectName.methodName() 
name = person.fullName(); // - - > John Doe

name = person.fullName; // - - > function() { return this.firstName + " " + this.lastName; } 
                  
  
                /* If  statements */

if (condition1) 
{
  //  block of code to be executed if condition1 is true
}
else if (condition2) 
{
  //  block of code to be executed if the condition1 is false and condition2 is true
} 
else 
{
  //  block of code to be executed if the condition1 is false and condition2 is false
}


              /* Switch statements */
                
switch(expression) 
{
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}  
// The switch expression is evaluated once.
// The value of the expression is compared with the values of each case.
// If there is a match, the associated block of code is executed.
// If there is no match, the default code block is executed.

                  
                  /* Functions */
// regular function & arrow function are the same
// arrow function is used write less syntax and make the code more elegant
                    
// Creating a function regular way                  
function sum(num1, num2=10)
 {
  // y is 10 if you use the function and not passed value  
  return num1 + num2;
 }
                  
 // Creating an arrow function   
 sum = (num1, num2) => num1+num2; // Arrow functions return values by default
 
 
 // Calling the function 
 sum(2,3) // - - > result is: 5
 
 // * With a regular function 'this' represents the object that calls the function
 // * With an arrow function 'this' represents the owner of the function
        
        
                        /*Loops */

// for - loops through a block of code a number of times
example = ["Bmw", "Tesla", "Audi"]
var i;
var l = example.length
for (i = 0; i < l; i++) 
{
  text += example[i] + "<br>"; 
}
// - - > Bmw
// - - > Tesla
// - - > Audi


// for/in - loops through the properties of an object
var person = {fname:"John", lname:"Doe", age:25};

var text = "";
var x;
for (x in person) 
{
  text += person[x];
}
// - - > John Doe 25 

// for/of - loops through the values of an iterable object
var string = 'txt';
var x;

for (x of string) 
{
  document.write(x + "<br >");
}
// - - > t
// - - > x
// - - > t


// while - loops through a block of code while a specified condition is true
while (condition) 
{
  // code block to be executed
} 

// do/while -                   
// loop will execute the code block once, before checking if the condition is true,
// then it will repeat the loop as long as the condition is true.
do 
{
  // code block to be executed
}
while (condition);


 
                    /* Break & Continue */
The break statement "jumps out" of the entire loop.

The continue statement "jumps over" one condition in the loop.

 
                  
                     /* Error handling */   
                         
// The try statement - allows you to define a block of code to be tested for errors while it is being executed.
// The catch statement - allows you to define a block of code to be executed, if an error occurs in the try block.                         
// The finally statement - lets you execute code, after try and catch, regardless of the result:
try 
{
  Block of code to try
}
catch(err) 
{
  Block of code to handle errors (executes when the error happen)
}
finally 
{
  Block of code to be executed regardless of the try / catch result
}

// The throw statement - allows you to create a custom error.
try 
{
    if(x == "") throw "empty";
    if(isNaN(x)) throw "not a number";
    x = Number(x);
    if(x < 5) throw "too low";
    if(x > 10) throw "too high";
}
  catch(err) 
{                  
    message.innerHTML = "Input is " + err;
}
  
                      /* Classes */
// creating class                     
class Car 
{
  constructor(brand)
  {
    this.carname = brand;
  }
}

// creating class object
mycar = new Car("Ford");      

               
                    /* Import & Export */
// in order to use elements from different modules 
import FunctionName from "./FileName"

// in order to allow element to get imported 
export default FunctionName


                         /* ES6 */

// The map() method creates a new array with the results of calling a function for every array element.
// The map() method calls the provided function once for each element in an array, in order.
var numbers = [4, 9, 16, 25];
var x = numbers.map(Math.sqrt) 


     /* let ,const and var */  
                 
/* Differences between let & var */             
// var is global variables 
// let & const are block variable 

var x = "Hello World";
{
  console.log(x);
}
// the console will show - - > Hello Woeld

let y = "Hello World"  
{
  console.log(y);
}
// Error


// Redeclaring Variables 

var x = 10;
// Here x is 10
{
  var x = 2;
  // Here x is 2
}
// Here x is 2


var y = 10;
// Here y is 10
{
  let y = 2;
  // Here y is 2
}
// Here y is 10

/* const */
// Variables defined with const behave like let variables, except they cannot be reassigned:

// You can create a const object:
const car = {type:"Fiat", model:"500", color:"white"};

// You can change a property:
car.color = "red";

// You can add a property:
car.owner = "Johnson";

// can't reassign constant object
car = {type:"Volvo", model:"EX60", color:"red"};  // ERROR

 
