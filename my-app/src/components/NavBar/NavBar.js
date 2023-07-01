import React from "react";
import "./NavBar.css";

const NavBar = () => {
    return (
        <nav className="navbar">
            <a href="/" className="logo">Logo</a>
            <ul className="nav-links">
                <li><a href="/About" className="about">About</a></li>
                <li><a href="/start" className="start">Get Started</a></li>
            </ul>
        </nav>
    );
};

export default NavBar