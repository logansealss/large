import { useSelector } from "react-redux"
import { useState } from "react"


import "./UserProfileImage.css"
import profilePic from "../../../images/ProfilePic.png"

export default function UserProfileImage() {

    const user = useSelector(state => state.session.user)
    const [imageURL, setImageURL] = useState(user.imageURL)

    return (

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
            <div>
                <input
                    style={{width: '100%'}}
                    type="text"
                    value={imageURL}
                >

                </input>
            </div>
        </div>
    )
}