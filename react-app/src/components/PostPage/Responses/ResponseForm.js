import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from 'react-router-dom'
import { createPostResponseThunk, updatePostResponseThunk } from "../../../store/responses"
import profilePic from "../../../images/ProfilePic.png"

export default function ResponseForm({ responseToUpdate, setDisplayForm }) {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const [focused, setFocused] = useState(!!responseToUpdate)

    let responseVal
    if (responseToUpdate) {
        responseVal = responseToUpdate.response
    }

    const [response, setResponse] = useState(responseVal || '')
    const [responseErr, setResponseErr] = useState()

    function clearForm() {
        setResponse('')
        setFocused(false)
        if (setDisplayForm) {
            setDisplayForm(false)
        }
    }

    async function onSubmit(e) {
        e.preventDefault()

        if (response.length > 255) {
            setResponseErr("Must be 255 characters or less")
            return;
        }

        if (responseToUpdate) {
            await dispatch(updatePostResponseThunk(responseToUpdate.id, { response }))
            clearForm()
        } else {
            await dispatch(createPostResponseThunk(postId, { response }))
            clearForm()
        }
    }

    useEffect(() => {

        if (response.length > 255) {
            setResponseErr("Must be 255 characters or less")
        } else {
            setResponseErr()
        }
    }, [response])

    return (

        <div
            className={responseToUpdate ? "response-form-container" : "response-form-container new-response"}
        >
            <div
                className="response-form-shadow-container"
            >
                {focused &&
                    // <div
                    //     className="response-form-name"
                    // >
                    //     {`${user.firstName} ${user.lastName}`}
                    // </div>
                    <div
                        className="response-author-profile-flex"
                    >
                        <div
                            className='profile-image-container'
                        >
                            <img
                                src={profilePic}
                            />
                        </div>
                        <div>
                            <div
                                className="response-author"
                            >
                                {`${user.firstName} ${user.lastName}`}
                            </div>
                        </div>
                    </div>
                }
                <form
                    id='response-form'
                    onSubmit={onSubmit}
                >
                    <div
                        id="response-input-container"
                        className='input-container'
                    >
                        <textarea
                            className={focused ? "response-form-textarea tall" : "response-form-textarea short"}
                            name='post'
                            onChange={(e) => setResponse(e.target.value)}
                            value={response}
                            placeholder="What are your thoughts?"
                            autoComplete="off"
                            onFocus={() => setFocused(true)}
                        ></textarea>
                    </div>
                    {focused &&
                        <div
                            className="response-form-footer-container"
                        >
                            <div
                                className="response-form-error"
                            >
                                <div>
                                    {responseErr ? responseErr : ''}
                                </div>
                            </div>
                            <div
                                className="response-submit-flex"
                            >
                                <div
                                    className="response-submit-cancel"
                                    onClick={clearForm}
                                >
                                    Cancel
                                </div>
                                <button
                                    id="post-form-button"
                                    className={(response.length <= 0) || !!responseErr ? "color-two opaque" : "color-two"}
                                    disabled={(response.length <= 0) || !!responseErr}
                                >
                                    Respond
                                </button>
                            </div>
                        </div>
                    }
                </form >
            </div >
        </div >
    )
}