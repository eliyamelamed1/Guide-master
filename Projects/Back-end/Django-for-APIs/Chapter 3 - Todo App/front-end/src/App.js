import './App.css';
import React, { Component } from 'react'; // new
import axios from 'axios'; // axios: api accessing package

// new
class App extends Component {
  state = {
    todos: []
  };

// new
componentDidMount() {
  this.getTodos();
}

// accesing api and saving data on the list
getTodos() {
  axios
    .get('http://127.0.0.1:8000/api/')
    .then(res => {
      this.setState({ todos: res.data });
    })
    .catch(err => {
      console.log(err);
    });
}  

render() {
  return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
          </div>
        ))}
      </div>
    );
  }
}


export default App;
