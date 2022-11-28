import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readUserPostsThunk } from "../../store/posts";
import { fetchPostClaps, fetchSinglePost, fetchPostResponses } from "../../store/userHelpers";
import { fetchFollowUser, fetchUnfollowUser } from "../../store/userHelpers";
import LoadingIcon from "../LoadingIcon/LoadingIcon";
import UserCard from "../UserCard/UserCard";
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
    const userId = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const author = useSelector(state => state.users[post.userId])
    const following = useSelector(state => state.follows.following)
    const claps = useSelector(state => state.claps)
    const posts = useSelector(state => state.posts.allPosts)
    const [scrollVisible, setScrollVisible] = useState(true)
    const [loaded, setLoaded] = useState(false)

    let userClap
    if (user) {
        userClap = Object.values(claps).find(clap => clap.userId === user.id)
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

            const result = await fetchSinglePost(postId, dispatch)

            if (result) {
                history.push('/')
            }
            await fetchPostResponses(postId, dispatch)
            await fetchPostClaps(postId, dispatch)
        })()
    }, [postId])

    useEffect(() => {

        if (!isEmptyObj(post)) {
            (async () => {
                await dispatch(readUserPostsThunk(post.userId))
                setLoaded(true)
            })()
        }
    }, [post])

    if (!loaded) {
        return (
            <LoadingIcon />
        )
    }

    return (
        <div id="post-page-flex">
            <div id="post-page-container">
                <div id="writer-card-container">
                    <div id="writer-card-flex">
                        <div id="writer-card-image-div">
                            <img
                                src={author.imageURL || profilePic}
                                alt={profilePic}
                                onError={e => { e.currentTarget.src = profilePic }}
                            />
                        </div>
                        <div id="writer-details-container">
                            <div id="writer-details">
                                <div
                                    className="writer-details-left"
                                >
                                    <UserCard
                                        user={author}
                                        className="writer-details-name"
                                        position="bottom"
                                    >
                                    </UserCard>
                                    {user && user.id !== author.id && (following[author.id] ?
                                        <button
                                            className="following user-follow-button"
                                            onClick={() => fetchUnfollowUser(author.id, dispatch)}
                                        >
                                            Following
                                        </button>
                                        :
                                        <button
                                            className="color-two user-follow-button"
                                            onClick={() => fetchFollowUser(author.id, dispatch)}
                                        >
                                            Follow
                                        </button>
                                    )
                                    }
                                </div>
                                {user && userClap &&
                                    <PostFooterMenu
                                        post={post}
                                        userClap={userClap}
                                    ></PostFooterMenu>
                                }
                                {
                                    user && user.id === author.id &&
                                    <PostFooterMenu
                                        post={post}
                                    ></PostFooterMenu>
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
                            <PostFooterClaps post={post} author={author}></PostFooterClaps>
                            <div className="post-scroll-divider-container">
                                <div className="post-scroll-divider">
                                </div>
                            </div>
                            <PostFooterResponses></PostFooterResponses>
                            {user && (userClap || author.id === user.id) && (
                                <>
                                    <div className="post-scroll-divider-container">
                                        <div className="post-scroll-divider">
                                        </div>
                                    </div>
                                    <div
                                        id="post-scroll-menu-flex"
                                    >
                                        <PostFooterMenu
                                            post={post}
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
                                <PostFooterClaps post={post} author={author}></PostFooterClaps>
                                <PostFooterResponses></PostFooterResponses>
                            </div>
                        </div>
                        <div

                        >
                            {user && userClap &&
                                <PostFooterMenu
                                    post={post}
                                    userClap={userClap}
                                >
                                </PostFooterMenu>
                            }
                            {user && author.id === user.id &&
                                <PostFooterMenu
                                    post={post}
                                ></PostFooterMenu>
                            }
                        </div>
                    </div>
                </div>
                <div
                    className="post-page-writer-footer"
                >
                    <div
                        className="post-page-writer-flex"
                    >
                        <div
                            className="post-page-writer-name"
                        >
                            {`More from ${author.firstName} ${author.lastName}`}
                        </div>
                        {user && user.id !== author.id && (following[author.id] ?
                            <button
                                className="following user-follow-button"
                                onClick={() => fetchUnfollowUser(author.id, dispatch)}
                            >
                                Following
                            </button>
                            :
                            <button
                                className="color-two user-follow-button"
                                onClick={() => fetchFollowUser(author.id, dispatch)}
                            >
                                Follow
                            </button>
                        )
                        }
                        {/* <button>
                            Follow
                        </button> */}
                    </div>
                    {author.about &&
                        <div
                            className="post-page-writer-about"
                        >
                            {author.about}
                        </div>
                    }
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