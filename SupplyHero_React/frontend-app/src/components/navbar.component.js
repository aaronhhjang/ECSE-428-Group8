import React, { Component } from 'react';
import { Link } from "react-router-dom";

export default class Navbar extends Component {

    render(){
        return(
            <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
                <Link to="/" className="navbar-brand">SupplyList</Link>
                <div className="collapse navbar-collapse">
                <ul className="navbar-nav mr-auto">
                    <li className="navbar-item">
                    <Link to="/register" className="nav-link">Register</Link>
                    </li>
                    <li className="navbar-item">
                    <Link to="/login" className="nav-link">Login</Link>
                    </li>
                    <li className="navbar_item">
                    <Link to="/logout" className="nav-link">Logout</Link>
                    </li>
                    <li className="navbar_item">
                    <Link to="/upload" className="nav-link">Upload</Link>
                    </li>
                   </ul>
                   </div></nav>
        )
    }


}