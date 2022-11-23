import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { logout } from "../../store/session";
import profilePic from "../../images/ProfilePic.png"
import "./NavbarDropdown.css"

export default function NavbarDropdown() {
    const dispatch = useDispatch();
    const [menuOpen, toggleMenuOpen] = useState(false);
    const user = useSelector(state => state.session.user);

    const signout = async (e) => {
        await dispatch(logout());
    };

    useEffect(() => {
        if (!menuOpen) return;

        const closeMenu = () => {
            toggleMenuOpen(false);
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [menuOpen]);

    function removeMenu() {
        toggleMenuOpen(false);
    }

    const popupMenuClass = menuOpen ? "popup-menu visible" : "popup-menu hidden"

    return (
        <>
            <div
                onClick={() => toggleMenuOpen(!menuOpen)}
                id='profile-image-container'
            >
                <img
                    src={user.imageURL || profilePic}
                    alt={profilePic}
                    onError={e => { e.currentTarget.src = profilePic }}
                />
            </div>
            <div
                className={popupMenuClass}
                id="popup"
                onClick={(e) => e.stopPropagation()}
            >
                <div
                    className="navbar-dropdown"
                >
                    <div>
                        {`${user.firstName} ${user.lastName}`}
                    </div>
                    <div>
                        {`${user.email}`}
                    </div>
                </div>
                <div
                    className="navbar-dropdown hover-dropdown"
                    onClick={signout}
                >
                    Sign out
                </div>
            </div>
        </>
    )
}