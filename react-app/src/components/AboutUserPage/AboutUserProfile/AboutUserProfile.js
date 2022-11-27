import { useSelector } from "react-redux"
import { useState, useEffect } from "react"


import "./AboutUserProfile.css"
import profilePic from "../../../images/ProfilePic.png"

export default function AboutUserProfile() {

    // const user = useSelector(state => state.session.user)
    const userId = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const [imageURL, setImageURL] = useState(user.imageURL || '')
    const [about, setAbout] = useState(user.about || '')
    const [imageURLError, setImageURLError] = useState('')
    const [aboutErr, setAboutErr] = useState('')
    const [submitted, setSubmitted] = useState(false)

    useEffect(() => {
        if(!submitted){
            return
        }

        if (imageURL.length > 255) {
            setImageURLError('Must be 255 characters or less')
        }
        else if (imageURL.length && !(/.\.(gif|jpe?g|tiff?|png|webp|bmp)$/i).test(imageURL)) {
            setImageURLError('Invalid image extension')
        }
        else {
            setImageURLError()
        }
    }, [imageURL])

    useEffect(() => {
        if(!submitted){
            return
        }

        if (about.length > 200) {
            setAboutErr('Must be 200 characters or less')
        }
        else {
            setAboutErr()
        }
    }, [about])

    return (
        <>
            <div
                className='user-profile-image'
            >
                <div
                    className="profile-pic-large"
                >
                    <img
                        src={user.imageURL || profilePic}
                        alt={profilePic}
                        onError={e => { e.currentTarget.src = profilePic }}
                    />
                </div>
                <div
                    className="user-profile-image-input"
                >
                    <input
                        type="text"
                        onChange={(e) => setImageURL(e.target.value)}
                        value={imageURL}
                    >
                    </input>
                </div>
            </div>
            <div
                className="user-profile-about-input"
            >
                <div>
                    {aboutErr}
                </div>
                <textarea
                    onChange={(e) => setAbout(e.target.value)}
                    value={about}
                >
                </textarea>
            </div>
            <button
                disabled={!(imageURL !== user.imageURL || about !== user.about) || imageURLError || aboutErr}
            >
                Update
            </button>
        </>
    )
}