import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState, useRef } from "react";

import { deletePostClapThunk } from "../../store/claps";
import { deletePostThunk } from "../../store/posts";
import { useHistory } from "react-router-dom";

import dots from "../../images/dots.svg"


export default function PostFooterMenu({ isTop, userClap }) {
    const dispatch = useDispatch()
    const ref = useRef()
    const history = useHistory()
    // const user = useSelector(state => state.session.user)
    const userId = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const post = useSelector(state => state.posts.singlePost)
    const claps = useSelector(state => state.claps)
    const [menuOpen, toggleMenuOpen] = useState(false);
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

    function menuOnClick(e) {
        toggleMenuOpen(cur => !cur)
    }

    async function deletePost() {
        dispatch(deletePostThunk(post.id))
        history.push('/')
    }

    function deleteConfirmation() {
        setConfirmDelete(true)
    }

    function editPost() {
        history.push(`/posts/${post.id}/edit`)
    }

    async function deleteUserClap() {
        dispatch(deletePostClapThunk(userClap.id))
    }

    const visibleMenu = menuOpen ? "post-menu visible" : "post-menu hidden"
    const topMenu = isTop ? " top" : ''
    const popupMenuClass = visibleMenu + topMenu




    return (
        <div
            className="post-menu-relative"
        >
            <div
                ref={ref}
                className="post-menu-container"
                onClick={menuOnClick}
            >
                <img
                    className="dots-img"
                    src={dots}
                />
                <div
                    className={popupMenuClass}
                    onClick={(e) => e.stopPropagation()}
                >
                    {user && user.id === post.userId && (
                        <>
                            <div
                                className="popup-menu-option"
                                onClick={editPost}
                            >
                                Edit this post
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
                                    onClick={deletePost}
                                >
                                    Confirm delete
                                </div>
                            )}
                        </>
                    )}
                    {user && user.id !== post.userId && (
                        <>
                            <div
                                className="popup-menu-option"
                                onClick={deleteUserClap}
                            >
                                Undo applause for this post
                            </div>
                        </>
                    )}
                </div>
            </div>
        </div>
    )
}