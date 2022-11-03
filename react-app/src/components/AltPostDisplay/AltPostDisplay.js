
import { Link } from "react-router-dom"

import { getMonthDay } from "../../utils/Dates"
import largePic from "../../images/Large.png"
import "./AltPostDisplay.css"

export default function AltPostDisplay({ post }) {

    return (
        <div
            className="alt-post-display"
        >
            <div
                className="alt-post-display-flex"
            >
                <div
                    className="alt-post-display-container"
                >
                    <div
                        className="alt-post-header-flex"
                    >
                        <div>
                            {`${post.writer.firstName} ${post.writer.lastName}`}
                        </div>
                        <div
                            className="post-content-spreader"
                        >
                            ·
                        </div>
                        <div>
                            {getMonthDay(post.createdAt)}
                        </div>
                    </div>
                    <Link
                        to={`/posts/${post.id}`}
                    >
                        <div
                            className="alt-post-content-flex"
                        >
                            <div
                                className="alt-post-content"
                            >
                                <div>
                                    <div
                                        className="alt-post-content-title"
                                    >
                                        {post.title}
                                    </div>
                                    <div
                                        className="alt-post-content-preview"
                                    >
                                        {post.preview}
                                    </div>
                                </div>
                            </div>
                            <div
                                className="alt-post-image-container"
                            >
                                <img
                                    src={post.imageURL || largePic}
                                    onError={(e) => e.currentTarget.src = largePic}
                                />
                            </div>
                        </div>
                    </Link>
                    <div
                        className="alt-post-image-container"
                    >
                        {`${post.readTime} min read`}
                    </div>
                </div>
            </div>
        </div>
    )
}