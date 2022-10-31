import { useEffect, useState } from "react"
import { useDispatch } from "react-redux"
import { useParams } from 'react-router-dom'
import { createPostResponseThunk } from "../../../store/responses"

export default function ResponseForm({ responseToUpdate }) {

    const { postId } = useParams()
    const dispatch = useDispatch()

    let responseVal
    if (responseToUpdate) {
        responseVal = responseToUpdate.response
    }

    const [response, setResponse] = useState(responseVal || '')
    const [responseErr, setResponseErr] = useState()
    const [submitted, setSubmitted] = useState(false)

    async function onSubmit(e) {
        e.preventDefault()
        setSubmitted(true)

        if(response.length > 255){
            setResponseErr("Must be 255 characters or less")
            return;
        }
        
        if(responseToUpdate){
            console.log("updated response")
        }else{
            console.log("created response")
            await dispatch(createPostResponseThunk(postId, {response}))
            setResponse('')
        }
    }

    useEffect(() => {

        if (submitted && response.length > 255) {
            setResponseErr("Must be 255 characters or less")
        } else {
            setResponseErr()
        }
    }, [response])

    return (
        <form
            id='response-form'
            onSubmit={onSubmit}
        >
            <div
                id="response-input-container"
                className='input-container'
            >
                <textarea
                    className="response-form-textarea"
                    name='post'
                    onChange={(e) => setResponse(e.target.value)}
                    value={response}
                    placeholder="What are your thoughts?"
                    autoComplete="off"
                ></textarea>
            </div>
            <div
                className="response-form-footer-container"
            >
                <div

                    // className={submitted && responseErr ? 'input-error' : 'input-error'}
                    className="response-form-error"
                >
                    <div>
                        {submitted && responseErr ? responseErr : ''}
                    </div>
                </div>
                <div
                    className="response-submit-flex"
                >
                    <button
                        id="post-form-button"
                        className={(response.length <= 0) || !!responseErr ? "color-two opaque" : "color-two"}
                        disabled={(response.length <= 0) || !!responseErr}
                    >
                        Respond
                    </button>
                </div>
            </div>
        </form >
    )
}