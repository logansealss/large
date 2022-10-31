import { useSelector } from "react-redux"

import { getMonthDay } from "../../../utils/Dates"
import dots from "../../../images/dots.svg"

export default function Response({response}) {

    const user = useSelector(state => state.session.user)

    return (
        <div
            className="response-container"
        >
            <div
                className="response-container-header"
            >
                <div
                    className="response-author-details"
                >
                    <div
                        className="response-author"
                    >
                        {`${response.user.firstName} ${response.user.lastName}`}
                    </div>
                    <div
                        className="response-date"
                    >
                        {`${getMonthDay(response.createdAt)}`}
                    </div>
                </div>
                {user && user.id === response.user.id && (
                    <div
                        
                    >
                        <img src={dots} />
                    </div>
                )}
            </div>
            <div
                className="response-response"
            >
                {response.response}
            </div>
        </div>
    )
}