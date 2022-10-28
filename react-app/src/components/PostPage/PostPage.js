import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import { isEmptyObj } from "../../utils/Objects";
import { getMonthDay } from "../../utils/Dates";
import { readSinglePostThunk } from "../../store/posts";
import "./PostPage.css"

export default function PostPage() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const post = useSelector(state => state.posts.singlePost)
    const user = useSelector(state => state.session.user)

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
                                    <div>
                                    <button>
                                        Manage post
                                    </button>
                                </div>}
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
            </div>
        </div>
    )
}