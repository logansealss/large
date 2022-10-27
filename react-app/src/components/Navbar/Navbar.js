import { Link, useHistory, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { logout } from '../../store/session';

import { isEmptyObj } from "../../utils/Objects";
import "./Navbar.css"
import mainLogo from "../../images/main-logo.png"

export default function Navbar() {

    const dispatch = useDispatch()
    const history = useHistory()
    const location = useLocation()
    const user = useSelector(state => state.session.user)
    const [isTop, setIsTop] = useState(true)

    function updateIsTop() {
        setIsTop(window.pageYOffset < 366)
    }

    const loggedIn = !isEmptyObj(user)

    useEffect(() => {
        if (typeof window !== "undefined") {
            if (!loggedIn) {
                window.addEventListener("scroll", updateIsTop)
            }
        }

        return () => window.removeEventListener("scroll", updateIsTop)
    }, [user])


    const signout = async (e) => {
        await dispatch(logout());
    };

    const signup = () => {
        history.push('/signup')
    }

    const buttonText = loggedIn ? "Sign out" : "Get started"
    const buttonClick = loggedIn ? signout : signup
    const writeLink = loggedIn ? "/new-post" : "/login"
    const navbarClass = (isTop && !loggedIn) ? "bottom-border color" : "bottom-border no-color"
    const navbarButtonClass = (location.pathname === '/' && isTop && !loggedIn) ? "color-one" : "color-two"


    return (
        <>
            <div
                id="navbar"
                className={navbarClass}
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
                                    <Link to={writeLink}>
                                        Write
                                    </Link>
                                </div>
                                {!loggedIn &&
                                    <div className="navbar-links">
                                        <Link to='/login'>
                                            Sign In
                                        </Link>
                                    </div>
                                }
                                <button
                                    id="navbar-button"
                                    className={navbarButtonClass}
                                    onClick={buttonClick}
                                >
                                    {buttonText}
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