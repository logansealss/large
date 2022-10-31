import { useSelector } from "react-redux"

import ReusableModal from "../../context/ReusableModal"
import Responses from "./Responses"
import "./Responses.css"
import chat from "../../images/chat.svg"

export default function PostFooterResponses() {

    const responses = useSelector(state => state.responses)

    return (
        <ReusableModal
            container={
                <div id="post-footer-responses">
                    <div id="post-footer-responses-flex">
                        <div className="svg-container">
                            <img src={chat} />
                        </div>
                        <div>
                            {Object.values(responses).length}
                        </div>
                    </div>
                </div>}
            bgClass='responses-modal-background'
        >
            <Responses></Responses>
        </ReusableModal>

    )
}