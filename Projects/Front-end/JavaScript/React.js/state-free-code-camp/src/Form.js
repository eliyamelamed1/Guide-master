import React, { Component } from 'react'
import FormComponent from './FormComponent'

export default class Form extends Component {
    constructor() {
        super()
        this.state = {
            firstName: "",
            lastName: "",
            textarea: "",
            gender: "",
            favColor: "",
            isVegan: false,
            isKosher: false,
        }
        this.handleChange = this.handleChange.bind(this)
    }

    // If handleChange used as Arrow function bind isn"t needed
    handleChange(event) {
        const {name, value, type, checked} = event.target 
        type === "checkbox" ? this.setState({ [name]: checked }) : this.setState({ [name]: value })
    }

    render() {
        return (
            <FormComponent
                handleChange = {this.handleChange}
                data = {this.state} 
                // {...this.state} - in FormComponent this.firstName
            />
        )
    }
}

