import { useDispatch, useSelector } from "react-redux"
import { useState, useEffect, useRef } from 'react'

import { deletePostResponsesThunk } from "../../../store/responses"
import { getMonthDay } from "../../../utils/Dates"
import dots from "../../../images/dots.svg"


export default function Response({ response }) {

    const ref = useRef()
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const [menuOpen, toggleMenuOpen] = useState(false);

    useEffect(() => {
        if (!menuOpen) return;

        console.log("menu open in useeffect")

        const closeMenu = () => {
            console.log("in close menu")
            toggleMenuOpen(false);
        };

        document.addEventListener('mouseup', closeMenu);

        return () => document.removeEventListener("mouseup", closeMenu);
    }, [menuOpen]);

    const popupMenuClass = menuOpen ? "response-menu visible" : "response-menu hidden"
    console.log("popupmenu class", popupMenuClass)

    function deleteResponse() {
        dispatch(deletePostResponsesThunk(response.id))
    }

    return (
        <div
            className="response-container"
        >
            <div
                className="response-container-header"
            >
                <div
                    className="response-author-details"
                >
                    <div
                        className="response-author"
                    >
                        {`${response.user.firstName} ${response.user.lastName}`}
                    </div>
                    <div
                        className="response-date"
                    >
                        {`${getMonthDay(response.createdAt)}`}
                    </div>
                </div>
                {user && user.id === response.user.id && (
                    <>
                        <div
                            onClick={() => toggleMenuOpen(!menuOpen)}
                            ref={ref}
                        >
                            <img src={dots} />
                        </div>
                        <div
                            className=""
                        >
                            <div
                                className={popupMenuClass}
                                onClick={(e) => e.stopPropagation()}
                            >
                                <div
                                    className="popup-menu-option"
                                    onClick={() => console.log("clicked update")}
                                >
                                    Update
                                </div>
                                <div
                                    className="popup-menu-option"
                                    onClick={() => console.log("clicked delete")}
                                >
                                    Delete
                                </div>
                            </div>
                        </div>
                    </>
                )}
            </div>
            <div
                className="response-response"
            >
                {response.response}
            </div>
        </div>
    )
}