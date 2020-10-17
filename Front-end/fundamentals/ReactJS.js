import React // in order to use JSX
import ReactDOM  

                      /* JSX */
// function that pass information to html                        
// ReactDom.render(what you want to render (JSX), where do you want to render) 
// render of multiple sepearted elements will result in Error, instead wrap them in mutual tag to maKe it work
function Text() { 
    const date = new Date()
    const hours = date.getHours()
    let timeOfDay
    if (hours < 12) {
      timeOfDay = "Morning"
    } else if (hours >= 12 & & hours < 17) {
      timeOfDay = "Afternoon"
    } else {
      timeOfDay = "Night"
    }
    
    const styles = {
      color: "ff8c00", 
      backgroundColor: "blue", 
      fontSize: "15rem"
    }
    
    return ( 
      <div> 
        <h1>Good {timeOfDay}</h1> // {this is where you can use JS in JSX}    
        <p style = {styles} >and happy holiday</p> 
      </div>
    ) 
}

// <FunctionName /> - format to call functions in JSX
ReactDom.render( <Text />, document.getElementById("IdName") )


