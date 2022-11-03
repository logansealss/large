import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readAllPostsThunk, readSinglePostThunk } from "../../store/posts";
import { readPostResponsesThunk } from "../../store/responses";
import AltPostDisplay from "../AltPostDisplay/AltPostDisplay";
import PostFooterMenu from "./PostFooterMenu";
import PostFooterClaps from "./PostFooterClaps";
import PostFooterResponses from "./PostFooterResponses";
import largePic from "../../images/Large.png"
import "./PostPage.css"

export default function PostPage() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const postFooterDetails = useRef()
    const post = useSelector(state => state.posts.singlePost)
    const user = useSelector(state => state.session.user)
    const responses = useSelector(state => state.session.responses)
    const posts = useSelector(state => state.posts.allPosts)
    const [scrollVisible, setScrollVisible] = useState(true)

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
                console.log(`post ${postId} not found`)
                history.push('/')
            }
            dispatch(readPostResponsesThunk(postId))
            dispatch(readAllPostsThunk())
        })()
    }, [postId])

    return (!isEmptyObj(post) &&
        <div id="post-page-flex">
            <div id="post-page-container">
                <div id="writer-card-container">
                    <div id="writer-card-flex">
                        <div id="writer-card-image-div">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png" />
                        </div>
                        <div id="writer-details-container">
                            <div id="writer-name-flex">
                                <div>
                                    {`${post.writer.firstName} ${post.writer.lastName}`}
                                </div>
                                {user &&
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
                            {user && (
                                <>
                                    <div className="post-scroll-divider-container">
                                        <div className="post-scroll-divider">
                                        </div>
                                    </div>
                                    <div
                                        id="post-scroll-menu-flex"
                                    >
                                        <PostFooterMenu
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
                            <PostFooterMenu></PostFooterMenu>
                        </div>
                    </div>
                </div>
                {Object.values(posts).map(post => (
                    <AltPostDisplay
                        key={post.id}
                        post={post}
                    >
                    </AltPostDisplay>
                ))}
            </div>
        </div>
    )
}