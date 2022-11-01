
import clap from "../../images/clap.svg"

export default function PostFooterClaps({post}) {

    return (
        <div id="post-footer-claps">
            <div id="post-footer-claps-flex">
                <div className="svg-container svg-claps">
                    <img src={clap} />
                </div>
                <div>
                    {post.numClaps}
                </div>
            </div>
        </div>
    )
}