import { Link, useHistory, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { logout } from '../../store/session';

import LoginForm from '../auth/LoginForm'
import SignupForm from '../auth/SignUpForm'
import AuthModalForm from "../auth/AuthModalForm";
import { isEmptyObj } from "../../utils/Objects";
import "./Navbar.css"
import "./AuthModal.css"
import mainLogo from "../../images/main-logo.png"
import ReusableModal from "../../context/ReusableModal";

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

    const buttonText = loggedIn ? "Sign out" : "Get started"
    const writeLink = loggedIn ? "/new-post" : "/login"

    let navbarClass = "bottom-border color"
    let navbarButtonClass = "color-one"

    if (location.pathname === '/') {
        if (loggedIn) {
            navbarButtonClass = "color-one"
            navbarClass = "bottom-border no-color"
        } else {
            if (!isTop) {
                navbarButtonClass = "color-two"
                navbarClass = "bottom-border no-color"
            }
        }
    } else {
        if (loggedIn) {
            navbarButtonClass = "color-one"
            navbarClass = "bottom-border no-color"
        } else {
            navbarClass = "bottom-border no-color"
            navbarButtonClass = "color-two"
        }
    }

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
                                {!loggedIn &&
                                    <>
                                        <ReusableModal
                                            displayText='Login'
                                            container={
                                                (<div className="navbar-links">
                                                    Sign In
                                                </div>)}
                                            bgClass='auth-modal'
                                        >
                                            <AuthModalForm formToDisplay={true}></AuthModalForm>
                                        </ReusableModal>
                                        <ReusableModal
                                            displayText='Get started'
                                            container={
                                                (<button
                                                    id="navbar-button"
                                                    className={navbarButtonClass}
                                                >
                                                    {buttonText}
                                                </button>
                                                )
                                            }
                                            bgClass='auth-modal'
                                        >
                                            <AuthModalForm formToDisplay={false}></AuthModalForm>
                                        </ReusableModal>
                                    </>
                                }
                                {loggedIn &&
                                    <>
                                        <div className="navbar-links">
                                            <Link to='/new-post'>
                                                Write
                                            </Link>
                                        </div>
                                        <div id='profile-image-container'>
                                            <img
                                                onClick={signout}
                                                src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" />
                                        </div>
                                    </>
                                }

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