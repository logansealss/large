import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readSinglePostThunk } from "../../store/posts";
import { createPostResponseThunk, readPostResponsesThunk } from "../../store/responses";
import PostFooterMenu from "./PostFooterMenu";
import PostFooterClaps from "./PostFooterClaps";
import PostFooterResponses from "./PostFooterResponses";
import dots from "../../images/dots.svg"
import "./PostPage.css"

export default function PostPage() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const postFooterDetails = useRef()
    const post = useSelector(state => state.posts.singlePost)
    const user = useSelector(state => state.session.user)
    const responses = useSelector(state => state.session.responses)
    const [scrollVisible, setScrollVisible] = useState(true)

    function managePost() {
        history.push(`/posts/${postId}/edit`)
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

    const loggedIn = !isEmptyObj(user)

    useEffect(() => {
        if (typeof window !== "undefined") {
            window.addEventListener("scroll", updateScrollVisible)
        }
        return () => window.removeEventListener("scroll", updateScrollVisible)
    }, [])

    useEffect(() => {

        (async () => {

            const result = await dispatch(readSinglePostThunk(postId))

            console.log("result of singlepostthunk", result)
            if (result) {
                console.log(`post ${postId} not found`)
                history.push('/')
            }
            dispatch(readPostResponsesThunk(postId))
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
                    <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png' />
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
                <div>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus commodo lobortis elit at mattis. Nullam semper mattis magna, at imperdiet nulla fringilla sit amet. Praesent sollicitudin congue mi, quis vehicula mauris facilisis et. Quisque malesuada eleifend dui eget gravida. Etiam tristique tristique elit a lobortis. Curabitur iaculis tincidunt odio. Maecenas fringilla neque diam, ac mollis elit venenatis id. Vivamus nec nulla ipsum. Proin ut efficitur ligula. Vivamus placerat lorem sit amet laoreet pharetra. Nam in odio et est ultricies ullamcorper vitae eget lectus.

                    Curabitur ut vestibulum nisi. Proin at volutpat libero. Curabitur id fringilla dui, vitae molestie augue. Etiam egestas nunc sed lorem fringilla, varius hendrerit purus elementum. In finibus nulla et lectus posuere cursus. Sed vel mollis nibh. Donec tincidunt laoreet porta. Donec a feugiat lectus, at euismod nisi. Suspendisse vulputate vehicula eros, id aliquet enim luctus in. Proin faucibus viverra erat vitae rhoncus. Vivamus arcu lectus, hendrerit sit amet vehicula vel, ultricies id lacus. In id ex sed ante blandit feugiat. Nam nisl justo, dignissim eget volutpat at, vehicula nec diam. Donec vitae risus molestie, finibus ante auctor, volutpat turpis. Nullam egestas, erat eu lobortis egestas, sapien enim consectetur mauris, eu facilisis purus augue at libero. Cras scelerisque semper dui a mattis.

                    Sed ultrices, sem non feugiat vehicula, elit magna tincidunt urna, nec blandit orci tortor ut neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam ultrices tempor fermentum. Vivamus ultricies neque auctor, malesuada magna ac, tincidunt elit. Curabitur laoreet arcu diam, eget elementum eros bibendum in. Vestibulum orci sem, egestas ut nisl non, venenatis volutpat enim. Integer sollicitudin tristique nisl, a mattis lectus posuere ac. Pellentesque condimentum venenatis orci, sit amet interdum turpis. Aliquam rhoncus sapien eu facilisis rhoncus. Sed pharetra sollicitudin velit quis vestibulum. Morbi quis felis vitae leo tincidunt placerat. Maecenas ut augue nec mi tempor gravida. Quisque vel neque sed ligula faucibus dignissim condimentum eget eros. In suscipit ante vitae sapien bibendum rutrum. Cras sed rhoncus lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

                    Donec scelerisque enim non neque posuere, eget semper urna dapibus. Vestibulum vel imperdiet leo. Nam massa purus, dapibus eu laoreet ut, pharetra eget nulla. Donec vitae cursus diam. Praesent aliquam placerat ipsum, id fringilla risus sagittis eget. Morbi pretium massa sit amet scelerisque iaculis. Nullam et pretium risus, ut consequat augue. Cras aliquet, dolor ut efficitur bibendum, ex ante malesuada quam, quis porttitor nisl velit non nulla. Curabitur rhoncus imperdiet justo et ultrices. Donec posuere et metus sed commodo. Mauris tellus eros, vestibulum ac vulputate vel, convallis non justo. Sed nec pulvinar sem, sed rutrum lorem. Aenean facilisis, odio eget gravida mollis, mauris nunc feugiat odio, vel dictum magna urna id libero. Suspendisse posuere, mauris eu commodo porta, turpis orci rutrum est, quis lacinia odio dui non nunc.

                    Cras pretium sed eros sed aliquet. Maecenas sagittis varius augue, vitae aliquet metus luctus sit amet. Donec consequat purus at dapibus placerat. Morbi sed nulla a lorem consequat tempor. Nullam et diam ligula. Donec non pulvinar metus. Proin tincidunt pharetra accumsan. Pellentesque a volutpat est, et imperdiet nulla. Nulla egestas tincidunt massa vel suscipit. Pellentesque eget sollicitudin turpis, ultricies ullamcorper dui. Nulla eget justo risus.
                </div>
            </div>
        </div>
    )
}