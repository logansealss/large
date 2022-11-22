import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readAllPostsThunk, readSinglePostThunk } from "../../store/posts";
import { readPostResponsesThunk } from "../../store/responses";
import { readPostClapsThunk } from "../../store/claps";
import { followUserThunk, unfollowUserThunk } from "../../store/follows"
import AltPostDisplay from "../AltPostDisplay/AltPostDisplay";
import PostFooterMenu from "./PostFooterMenu";
import PostFooterClaps from "./PostFooterClaps";
import PostFooterResponses from "./PostFooterResponses";
import largePic from "../../images/Large.png"
import profilePic from "../../images/ProfilePic.png"
import "./PostPage.css"

export default function PostPage() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const postFooterDetails = useRef()
    const post = useSelector(state => state.posts.singlePost)
    const user = useSelector(state => state.session.user)
    const following = useSelector(state => state.follows.following)
    const claps = useSelector(state => state.claps)
    const posts = useSelector(state => state.posts.allPosts)
    const [scrollVisible, setScrollVisible] = useState(true)

    let userClap
    if (user) {
        userClap = Object.values(claps).find(clap => clap.user.id === user.id)
    }

    function isInViewport(rect) {
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function updateScrollVisible() {
        if (postFooterDetails.current) {
            const rect = postFooterDetails.current.getBoundingClientRect()
            setScrollVisible(!isInViewport(rect) && rect.bottom > 75)
        }
    }

    useEffect(() => {
        if (typeof window !== "undefined") {
            window.addEventListener("scroll", updateScrollVisible)
        }
        return () => window.removeEventListener("scroll", updateScrollVisible)
    }, [])

    useEffect(() => {

        (async () => {

            const result = await dispatch(readSinglePostThunk(postId))

            if (result) {
                history.push('/')
            }
            dispatch(readPostResponsesThunk(postId))
            dispatch(readPostClapsThunk(postId))
            dispatch(readAllPostsThunk())
        })()
    }, [postId])

    return (!isEmptyObj(post) &&
        <div id="post-page-flex">
            <div id="post-page-container">
                <div id="writer-card-container">
                    <div id="writer-card-flex">
                        <div id="writer-card-image-div">
                            <img src={profilePic} />
                        </div>
                        <div id="writer-details-container">
                            <div id="writer-details">
                                <div
                                    className="writer-details-left"
                                >
                                    <div
                                        className="writer-details-name"
                                    >
                                        {`${post.writer.firstName} ${post.writer.lastName}`}
                                    </div>

                                    {user && (following[post.writer.id] ? 
                                        <button
                                            className="following user-follow-button"
                                            onClick={() => dispatch(unfollowUserThunk(post.writer.id))}
                                        >
                                            Following
                                        </button>
                                        :
                                        <button
                                        className="color-two user-follow-button"
                                            onClick={() => dispatch(followUserThunk(post.writer.id))}
                                        >
                                            Follow
                                        </button>
                                        )
                                    }
                                </div>
                                {user && userClap &&
                                    <PostFooterMenu
                                        userClap={userClap}
                                    ></PostFooterMenu>
                                }
                                {
                                    user && user.id === post.writer.id &&
                                    <PostFooterMenu></PostFooterMenu>
                                }
                            </div>
                            <div>
                                <div id="writer-post-details">
                                    <div>
                                        {getMonthDay(post.createdAt)}
                                    </div>
                                    <div className="post-content-spreader">
                                        ·
                                    </div>
                                    <div>
                                        {`${post.readTime} min read`}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="post-title">
                    {post.title}
                </div>
                <div id='post-subtitle'>
                    {post.subtitle && post.subtitle}
                </div>
                <div id="post-image-container">
                    <img
                        src={post.imageURL || largePic}
                        alt={largePic}
                        onError={e => { e.currentTarget.src = largePic }}
                    />
                </div>
                <div id="post-content">
                    {post.post}
                </div>
                <div
                    id="post-scroll-container"
                    className={scrollVisible ? "" : "hidden"}
                >
                    <div id="post-scroll-background">
                        <div id="post-footer-interactions-flex">
                            <PostFooterClaps post={post}></PostFooterClaps>
                            <div className="post-scroll-divider-container">
                                <div className="post-scroll-divider">
                                </div>
                            </div>
                            <PostFooterResponses></PostFooterResponses>
                            {user && (userClap || post.writer.id === user.id) && (
                                <>
                                    <div className="post-scroll-divider-container">
                                        <div className="post-scroll-divider">
                                        </div>
                                    </div>
                                    <div
                                        id="post-scroll-menu-flex"
                                    >
                                        <PostFooterMenu
                                            userClap={userClap}
                                            isTop={true}
                                        ></PostFooterMenu>
                                    </div>
                                </>
                            )}
                        </div>
                    </div>
                </div>
                <div
                    ref={postFooterDetails}
                    id="post-footer-details">
                    <div id="post-footer-details-flex">
                        <div id="post-footer-interactions">
                            <div id="post-footer-interactions-flex">
                                <PostFooterClaps post={post}></PostFooterClaps>
                                <PostFooterResponses></PostFooterResponses>
                            </div>
                        </div>
                        <div

                        >
                            {user && userClap &&
                                <PostFooterMenu
                                    userClap={userClap}
                                >
                                </PostFooterMenu>
                            }
                            {user && post.writer.id === user.id &&
                                <PostFooterMenu></PostFooterMenu>
                            }
                        </div>
                    </div>
                </div>
                {Object.values(posts).map(post => post.id !== +postId ? (
                    <AltPostDisplay
                        key={post.id}
                        post={post}
                    >
                    </AltPostDisplay>
                ) : null)}
            </div>
        </div>
    )
}