import React, {Component} from "react";
import {Link, Redirect} from "react-router-dom";
import axios from 'axios';


class Register extends Component {

  state = {};

    register = (username, password) => {
        axios.post('/api/auth/register/', {
            username: username,
            password: password
          })
          .then(res => {
            if (res.status === 200) {
              window.token = res.data.token;
            } else if (res.status === 401 || res.status === 403) {
              console.log("AUTHENTICATION_ERROR");
              throw res.data;
            }
      })
    }
    onSubmit = e => {
    e.preventDefault();
    this.register(this.state.username, this.state.password);
  }

  render() {
    if (!window.token === "") {
      return <Redirect to="/" />
    }
    return (
      <form onSubmit={this.onSubmit}>
        <fieldset>
          <legend>Register</legend>
          <p>
            <label htmlFor="username">Username </label>
            <input
              type="text" id="username"
              onChange={e => this.setState({username: e.target.value})} />
          </p>
          <p>
            <label htmlFor="password">Password </label>
            <input
              type="password" id="password"
              onChange={e => this.setState({password: e.target.value})} />
          </p>
          <p>
            <button type="submit">Register</button>
          </p>

          <p>
            Already have an account? <Link to="/login">Login</Link>
          </p>
        </fieldset>
      </form>
    )
  }
}


export default Register;