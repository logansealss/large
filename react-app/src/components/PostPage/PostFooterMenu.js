import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState, useRef } from "react";
import { deletePostThunk } from "../../store/posts";
import { useHistory } from "react-router-dom";

import dots from "../../images/dots.svg"


export default function PostFooterMenu() {
    const dispatch = useDispatch()
    const ref = useRef()
    const history = useHistory()
    const user = useSelector(state => state.session.user)
    const post = useSelector(state => state.posts.singlePost)
    const [menuOpen, toggleMenuOpen] = useState(false);
    const [displayForm, setDisplayForm] = useState(false)

    useEffect(() => {
        if (!menuOpen) return;

        const closeMenu = (e) => {

            if (ref.current && !ref.current.contains(e.target) && ref.current !== e.target) {
                toggleMenuOpen(cur => !cur);
            }
        };

        document.addEventListener('click', closeMenu);

        return () => document.removeEventListener("click", closeMenu);
    }, [menuOpen]);

    function menuOnClick(e) {
        toggleMenuOpen(cur => !cur)
    }

    async function deletePost() {
        await dispatch(deletePostThunk(post.id))
        history.push('/')
    }

    function editPost() {
        history.push(`/posts/${post.id}/edit`)
    }


    const popupMenuClass = menuOpen ? "post-menu visible" : "post-menu hidden"


    return (
        <div
            className="post-menu-relative"
        >
            <div
                ref={ref}
                className="post-menu-container"
                onClick={menuOnClick}
            >
                <img src={dots} />
                <div
                    className={popupMenuClass}
                    onClick={(e) => e.stopPropagation()}
                >
                    {user && user.id === post.writer.id && (
                        <>
                            <div
                                className="popup-menu-option"
                                onClick={editPost}
                            >
                                Edit this post
                            </div>
                            <div
                                className="popup-menu-option"
                                onClick={deletePost}
                            >
                                Delete
                            </div>
                        </>
                    )}
                    {user && user.id !== post.writer.id && (
                        <>
                            <div
                                className="popup-menu-option"
                                // onClick={editPost}
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