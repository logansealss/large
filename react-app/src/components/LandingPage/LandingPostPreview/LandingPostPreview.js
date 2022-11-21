

import { Link } from "react-router-dom";

import UserCard from "../../UserCard/UserCard";
import { getMonthDay } from "../../../utils/Dates";
import largePic from "../../../images/Large.png"
import profilePic from "../../../images/ProfilePic.png"
import "./LandingPostPreview.css"

export default function LandingPostPreview({ post }) {

    const monthDayStr = getMonthDay(post.createdAt)

    return (
        <div className="post-container">
            <div className="post-container-padding">
                <div className="post-content-flex">
                    <div className="post-content">
                        <div className="post-content-container">
                            <div
                                className="post-content-header-flex"
                            >
                                <div
                                    className="profile-pic-small"
                                >
                                    <img
                                        src={profilePic}
                                    />
                                </div>
                                {/* <div className="post-content-name">
                                    {`${post.writer.firstName} ${post.writer.lastName}`}
                                </div> */}

                                {/* TODO: complete hover effect for user cards */}
                                <UserCard 
                                    user={post.writer}
                                    className="post-content-name"
                                ></UserCard>
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