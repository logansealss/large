import { Link } from "react-router-dom";

import "./Navbar.css"
import mainLogo from "../../images/main-logo.png"

export default function Navbar() {
    return (
        <>
            <div
                id="navbar"
                className="bottom-border"
            >
                <div id="navbar-container-flex">
                    <div id="navbar-menu-container">
                        <div id="navbar-menu-container-flex">
                            <div id="navbar-logo">
                                <Link to="/">
                                    <img id="navbar-image" src={mainLogo} />
                                </Link>
                            </div>
                            <div id='navbar-menu-container-flex'>
                                <div className="navbar-links">
                                    <a href="https://github.com/logansealss" target="_blank">
                                        Github
                                    </a>
                                </div>
                                <div className="navbar-links">
                                    <a href="https://www.linkedin.com/in/logan-seals-b91454251/" target="_blank">
                                        LinkedIn
                                    </a>
                                </div>
                                <div className="navbar-links">
                                    <Link>
                                        Sign In
                                    </Link>
                                </div>
                                <button
                                    id="navbar-button"
                                    className="navbar-header-button"
                                >
                                    Get Started
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="margin-for-navbar">
            </div>
        </>
    )
}