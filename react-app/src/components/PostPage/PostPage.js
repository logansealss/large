import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readSinglePostThunk } from "../../store/posts";
import clap from "../../images/clap.svg"
import chat from "../../images/chat.svg"
import dots from "../../images/dots.svg"
import "./PostPage.css"

export default function PostPage() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const post = useSelector(state => state.posts.singlePost)
    const user = useSelector(state => state.session.user)

    function managePost() {
        history.push(`/posts/${postId}/edit`)
    }

    useEffect(() => {

        (async () => {

            const result = dispatch(readSinglePostThunk(postId))

            if (!result) {
                console.log(`post ${postId} not found`)
                history.push('/')
            }
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
                                {user && user.id === post.writer.id &&
                                    <div className="svg-container">
                                        <img
                                            onClick={managePost}
                                            src={dots}
                                        ></img>
                                    </div>
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
                <div id="post-scroll-container">
                    <div id="post-scroll-background">
                        <div id="post-footer-interactions-flex">
                            <div id="post-footer-claps">
                                <div id="post-footer-claps-flex">
                                    <div className="svg-container">
                                        <img src={clap} />
                                    </div>
                                    <div>
                                        {post.numClaps}
                                    </div>
                                </div>
                            </div>
                            <div id="post-footer-responses">
                                <div id="post-footer-responses-flex">
                                    <div className="svg-container">
                                        <img src={chat} />
                                    </div>
                                    <div>
                                        {post.numResponses}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="post-footer-details">
                    <div id="post-footer-details-flex">
                        <div id="post-footer-interactions">
                            <div id="post-footer-interactions-flex">
                                <div id="post-footer-claps">
                                    <div id="post-footer-claps-flex">
                                        <div className="svg-container">
                                            <img src={clap} />
                                        </div>
                                        <div>
                                            {post.numClaps}
                                        </div>
                                    </div>
                                </div>
                                <div id="post-footer-responses">
                                    <div id="post-footer-responses-flex">
                                        <div className="svg-container">
                                            <img src={chat} />
                                        </div>
                                        <div>
                                            {post.numResponses}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <div className="svg-container">
                                <img src={dots}></img>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}