import { useSelector } from "react-redux"
import { useState } from "react"


import "./UserProfileImage.css"
import profilePic from "../../../images/ProfilePic.png"

export default function UserProfileImage() {

    const user = useSelector(state => state.session.user)
    const [imageURL, setImageURL] = useState(user.imageURL)
    const [about, setAbout] = useState(user.about)

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
            <div>
                <textarea
                    onChange={(e) => setAbout(e.target.value)}
                    value={about}
                >
                </textarea>
            </div>
            <div>
                Update
            </div>
        </>
    )
}