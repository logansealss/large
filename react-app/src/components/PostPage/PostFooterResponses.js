
import { useSelector } from "react-redux"
import chat from "../../images/chat.svg"

export default function PostFooterResponses() {

    const responses = useSelector(state => state.responses)

    return (
        <div id="post-footer-responses">
            <div id="post-footer-responses-flex">
                <div className="svg-container">
                    <img src={chat} />
                </div>
                <div>
                    {Object.values(responses).length}
                </div>
            </div>
        </div>
    )
}