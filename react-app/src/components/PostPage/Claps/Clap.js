
import profilePic from "../../../images/ProfilePic.png"
import "./Clap.css"

export default function Clap({ clap, user }) {
    return (
        <div
            className="clap-container"
        >
            <div
                className="clap-container-flex"
            >
                <div
                    className='profile-image-container'
                >
                    <img
                        src={user.imageURL || profilePic}
                        alt={profilePic}
                        onError={e => { e.currentTarget.src = profilePic }}
                    />
                </div>
                <div
                    className="clap-name-container"
                >
                    {`${user.firstName} ${user.lastName}`}
                </div>
            </div>
        </div>
    )
}