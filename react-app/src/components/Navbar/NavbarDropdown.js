import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { logout } from "../../store/session";
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

        console.log("menu open in useeffect")

        const closeMenu = () => {
            console.log("in close menu")
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
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png"
                />
            </div>
            <div
                className={popupMenuClass}
                id="popup"
                onClick={(e) => e.stopPropagation()}
            >
                <div
                    className="popup-menu-option"
                    onClick={signout}
                >
                    Sign out
                </div>
            </div>
        </>
    )
}