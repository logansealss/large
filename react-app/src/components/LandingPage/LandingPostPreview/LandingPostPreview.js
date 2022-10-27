
import "./LandingPostPreview.css"

export default function LandingPostPreview({ post }) {

    const postMonth = post.createdAt.slice(8, 11);
    const postDay = post.createdAt.slice(5, 7);

    console.log("image url", post.imageURL)


    return (
        <div className="post-container">
            <div className="post-container-padding">
                <div className="post-content-flex">
                    <div className="post-content">
                        <div className="post-content-name">
                            {`${post.writer.firstName} ${post.writer.lastName}`}
                        </div>
                        <div className="post-content-title">
                            {`${post.title}`}
                        </div>
                        <div className="post-content-preview">
                            {`${post.preview}`}
                        </div>
                        <div className="post-content-details">
                            <div>
                                {`${postMonth} ${postDay}`}
                            </div>
                            <div className="post-content-spreader">
                                ·
                            </div>
                            <div>
                                {`${post.readTime} min read`}
                            </div>
                        </div>
                    </div>
                    <div className="post-image-container">
                        {/* <img src={post.imageURL} /> */}
                        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png' />
                    </div>
                </div>
            </div>
        </div>
    )
}