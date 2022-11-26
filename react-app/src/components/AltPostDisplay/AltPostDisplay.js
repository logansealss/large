
import { Link } from "react-router-dom"

import { getMonthDay } from "../../utils/Dates"
import largePic from "../../images/Large.png"
import profilePic from "../../images/ProfilePic.png"
import "./AltPostDisplay.css"

export default function AltPostDisplay({ post, showWriter }) {

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
                        {showWriter &&
                            <>
                                <div
                                    className="profile-pic-small"
                                >
                                    <img
                                        src={post.writer.imageURL || profilePic}
                                        alt={profilePic}
                                        onError={e => { e.currentTarget.src = profilePic }}
                                    />
                                </div>
                                <div>
                                    {`${post.writer.firstName} ${post.writer.lastName}`}
                                </div>
                                <div
                                    className="post-content-spreader"
                                >
                                    ·
                                </div>
                            </>
                        }
                        <div
                            className="alt-post-date"
                        >
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
                        className="alt-post-data"
                    >
                        {`${post.readTime} min read`}
                    </div>
                </div>
            </div>
        </div>
    )
}