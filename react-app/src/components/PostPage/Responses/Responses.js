import { useSelector } from "react-redux"

import Response from './Response'
import ResponseForm from "./ResponseForm"

export default function Responses() {

    const responses = useSelector(state => state.responses)
    const user = useSelector(state => state.session.user)

    return (
        <div
            id="response-modal-content"
        >
            <div
                id="response-modal-header"
            >
                {`Responses (${Object.values(responses).length})`}
            </div>
            {user && (
                <>
                    <div
                        className="response-form-bottom-margin"
                    >
                        <ResponseForm></ResponseForm>
                    </div>
                    <div
                        className="response-form-bottom-border"
                    ></div>
                </>
            )}
            {Object.values(responses).map(response => (
                <Response
                    response={response}
                    key={response.id}
                ></Response>
            ))}

        </div>
    )
}