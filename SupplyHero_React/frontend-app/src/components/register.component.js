import React, { Component } from 'react';

export default class Register extends Component{
    constructor(props){
        super(props);

        this.onChangeUsername = this.onChangeUsername.bind(this);
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            username: '',
            password: '',
        }
    }

    onChangeUsername(e){
        this.setState({
            username: e.target.value
        });
    }

    onChangePassword(e){
        this.setState({
            password: e.target.value
        });
    }

    onSubmit(e){
        e.preventDefault();

        const user = {
            username:this.state.username,
            password:this.state.password,
        }

        console.log(user);

        this.setState({
            username:'',
            password:'',
        })

        fetch('http://localhost:8000/register', {
          method: "POST",
          headers: {
            Accept: "application/json","Content-Type": "application/json"
          },
          body: JSON.stringify({
            email: "test@gmail.com",
            password: "mypassword"
          })
        })
        .then(function(response) {
            return response.json();
        })
        .catch(e => {
            console.log(e)
        })
        //window.location = '/' // reroutes to home page after submitting

    }



    render(){
        return(
            <div>
              <h3>Register</h3>
              <form onSubmit={this.onSubmit}>
                <div className="form-group">
                    <label>Username: </label>
                    <input
                        type="text"
                        required
                        value={this.state.username}
                        placeholder="Enter your email"
                        className="form-control"
                        onChange={this.onChangeUsername}
                    />
                    <label>Password: </label>
                    <input
                        type="text"
                        required
                        value={this.state.password}
                        placeholder="Enter your password"
                        className="form-control"
                        onChange={this.onChangePassword}
                    />
                    </div>
                    <div className="form-group">
                <input type="submit" value="Register" onClick={this.onSubmit} className="btn btn-primary" />
                </div>
              </form>
            </div>
        )
    }
}