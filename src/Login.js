import React, {Component} from "react";
import {Link, Redirect} from "react-router-dom";
import axios from 'axios';

window.token= "";
class Login extends Component {
    state = {
    isLoggedIn:false,
    token:""
    };


    login = (username, password) => {
        axios.post('/api/auth/login/', {
            username: username,
            password: password
          })
          .then(res => {
            if (res.status === 200) {
              this.setState({isLoggedIn: true});
              window.token = res.data.token;
            } else if (res.status === 401 || res.status === 403) {
              console.log("AUTHENTICATION_ERROR");
              throw res.data;
            }
      })
    }
    onSubmit = e => {
    e.preventDefault();
    this.login(this.state.username, this.state.password);
  }

  render() {
    if (this.state.isLoggedIn) {
      return <Redirect to="/" />
    }
    return (
    <div>
        <div>
            <div>
                <h2>Welcome to Aggregator</h2>
                <p>Please log in below, or click the link below to register a new account.</p>
            </div>
        </div>

      <form onSubmit={this.onSubmit}>
        <fieldset>
          <legend>Login</legend>
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
            <button type="submit">Login</button>
          </p>
          <p>Don't have an account? <Link to="/register">Register</Link></p>
        </fieldset>
      </form>
      </div>
    )
  }
}

export default Login;