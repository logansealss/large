import { useDispatch, useSelector } from "react-redux"
import { useState, useEffect, useRef } from 'react'

import ResponseForm from "./ResponseForm"
import { deletePostResponsesThunk } from "../../../store/responses"
import { getMonthDay } from "../../../utils/Dates"
import dots from "../../../images/dots.svg"


export default function Response({ response }) {

    const dispatch = useDispatch()
    const ref = useRef()
    const user = useSelector(state => state.session.user)
    const [menuOpen, toggleMenuOpen] = useState(false);
    const [displayForm, setDisplayForm] = useState(false)
    const [confirmDelete, setConfirmDelete] = useState(false)

    useEffect(() => {
        if (!menuOpen) return;

        const closeMenu = (e) => {

            if (ref.current && !ref.current.contains(e.target) && ref.current !== e.target) {
                toggleMenuOpen(cur => !cur);
                setConfirmDelete(false)
            }
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [menuOpen]);

    const popupMenuClass = menuOpen ? "response-menu visible" : "response-menu hidden"

    function deleteResponse() {
        dispatch(deletePostResponsesThunk(response.id))
    }

    function menuOnClick(e) {
        toggleMenuOpen(cur => !cur)
    }

    function editResponse() {
        setDisplayForm(true)
        toggleMenuOpen(cur => !cur)
    }

    async function deleteResponse() {
        await dispatch(deletePostResponsesThunk(response.id))
        toggleMenuOpen(cur => !cur)
    }

    function deleteConfirmation() {
        setConfirmDelete(true)
    }

    return (
        <div
            className="response-container"
        >
            {displayForm && <ResponseForm responseToUpdate={response} setDisplayForm={setDisplayForm}></ResponseForm>}
            {!displayForm && (
                <>
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
                            <div
                                className="response-menu-relative"
                            >
                                <div
                                    ref={ref}
                                    className="response-menu-container"
                                    onClick={menuOnClick}
                                >
                                    <img src={dots} />
                                    <div
                                        className={popupMenuClass}
                                        onClick={(e) => e.stopPropagation()}
                                    >
                                        <div
                                            className="popup-menu-option"
                                            onClick={editResponse}
                                        >
                                            Edit this response
                                        </div>
                                        {!confirmDelete && (
                                            <div
                                                className="popup-menu-option"
                                                onClick={deleteConfirmation}
                                            >
                                                Delete
                                            </div>
                                        )}
                                        {confirmDelete && (
                                            <div
                                                className="popup-menu-option confirm-delete"
                                                onClick={deleteResponse}
                                            >
                                                Confirm delete
                                            </div>
                                        )}
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                    <div
                        className="response-response"
                    >
                        {response.response}
                    </div>
                </>
            )}
        </div>
    )
}