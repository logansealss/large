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

    const popupMenuClass = menuOpen ? "popup-menu popup-menu-visible" : "popup-menu popup-menu-hidden"

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


        // <div
        //     className="menu-button-container"
        // >
        //     <div>
        //         <button
        //             className='menu-button'
        //             onClick={() => toggleMenuOpen(!menuOpen)}
        //         >
        //             <div className='icon-container'>
        //                 <i className="fa-solid fa-bars fa-1x"></i>
        //                 <i className="fa-solid fa-user fa-2x"></i>
        //             </div>
        //         </button>
        //         <div
        //             className={popupMenuClass}
        //             id="popup"
        //         >
        //             {user ? (
        //                 <>
        //                     <div
        //                         className="popup-menu-option-no-pointer"
        //                     >
        //                         {user.username}
        //                     </div>
        //                     <div
        //                         id="bottom-border"
        //                         className="popup-menu-option-no-pointer"
        //                     >
        //                         {user.email}
        //                     </div>
        //                     <div
        //                         className="popup-menu-option"
        //                         onClick={() => history.push("/myspots")}
        //                     >
        //                         My spots
        //                     </div>
        //                     <div
        //                         className="popup-menu-option"
        //                         onClick={() => history.push("/myreviews")}
        //                     >
        //                         My reviews
        //                     </div>
        //                     <div
        //                         className="popup-menu-option"
        //                         onClick={() => history.push("/createspot")}
        //                     >
        //                         Create spot
        //                     </div>
        //                     <div
        //                         className="popup-menu-option"
        //                         onClick={logout}
        //                     >Log out
        //                     </div>
        //                 </>
        //             )
        //                 : (
        //                     <>
        //                         <LoginFormModal afterSubmission={removeMenu} className="popup-menu-option" />
        //                         <SignupFormModal afterSubmission={removeMenu} className="popup-menu-option" />
        //                     </>
        //                 )
        //             }
        //         </div>
        //     </div>
        // </div >
    )

}