

import { Link } from "react-router-dom";
import { getMonthDay } from "../../../utils/Dates";
import largePic from "../../../images/Large.png"
import "./LandingPostPreview.css"

export default function LandingPostPreview({ post }) {

    const monthDayStr = getMonthDay(post.createdAt)

    return (
        <div className="post-container">
            <div className="post-container-padding">
                <div className="post-content-flex">
                    <div className="post-content">
                        <div className="post-content-container">

                            <div className="post-content-name">
                                {`${post.writer.firstName} ${post.writer.lastName}`}
                            </div>
                            <Link to={`/posts/${post.id}`}>
                                <div className="post-content-title">
                                    {`${post.title}`}
                                </div>
                                <div className="post-content-preview">
                                    {`${post.preview}`}
                                </div>
                                <div className="post-content-details">
                                    <div>
                                        {monthDayStr}
                                    </div>
                                    <div className="post-content-spreader">
                                        ·
                                    </div>
                                    <div>
                                        {`${post.readTime} min read`}
                                    </div>
                                </div>
                            </Link>
                        </div>
                    </div>
                    <Link to={`/posts/${post.id}`}>
                        <div className="post-image-container">
                            <img
                                src={post.imageURL || largePic}
                                alt={largePic}
                                onError={e => { e.currentTarget.src = largePic }}
                            />
                        </div>
                    </Link>
                </div>
            </div>
        </div>
    )
}