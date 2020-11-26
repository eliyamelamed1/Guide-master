import React from "react"

export default function FormComponent(props) {
    return (
        <main>
            <form>
                <input 
                    type="text" 
                    value = {props.data.firstName} 
                    name="firstName" 
                    placeholder="First Name" 
                    onChange={props.handleChange} 
                />
                <br />
                <input 
                    type="text" 
                    value={props.data.lastName} 
                    name="lastName" 
                    placeholder="Last Name" 
                    onChange={props.handleChange} 
                />
                <br />
                <textarea 
                    name="textarea"
                    value={props.data.textarea}
                    placeholder="Type something"
                    onChange={props.handleChange}     
                />
                <br />
                <>
                    <input 
                        type="checkbox" 
                        name="isVegan" 
                        checked={props.data.isVegan}
                        onChange={props.handleChange}
                    /> Is vegan?
                    <input 
                        type="checkbox" 
                        name="isKosher" 
                        checked={props.data.isKosher}
                        onChange={props.handleChange}
                    /> Is kosher?
                </>
                <br />
                <>
                    <input 
                        type="radio" 
                        name="gender"
                        value="male" 
                        checked={props.data.gender === "male"}
                        onChange={props.handleChange}
                    /> Male
                </>
                <br />
                <>
                    <input 
                        type="radio" 
                        name="gender"
                        value="female" 
                        checked={props.data.gender === "female"}
                        onChange={props.handleChange}
                    /> female
                </>          
                <br />
                <>Favorite color: 
                    <select 
                        value={props.data.favColor} 
                        onChange={props.handleChange}
                        name="favColor"
                    >

                        <option >---Please choose favorie color---</option>
                        <option value="blue"> blue</option>
                        <option value="green"> green </option>
                        <option value="red"> red </option>
                        <option value="orange"> orange </option>
                        <option value="yellow"> yellow </option>
                    </select>
                </>
                <hr />
                <h5>full name: {props.data.firstName} {props.data.lastName}</h5>
                <h5>gender:  {props.data.gender} </h5>
                <h5>favorite color: {props.data.favColor} </h5>
                <h5>
                    Dietery restictions:
                    <br />
                    Vegan : {props.data.isVegan ? "Yes" : "No"}
                    <br />
                    Kosher : {props.data.isKosher ? "Yes" : "No"} 
                </h5>
                <button>Submit</button>
            </form>
        </main>
    )
}

