
import profilePic from "../../../images/ProfilePic.png"
import "./Clap.css"

export default function Clap({ clap }) {
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
                        src={clap.user.imageURL || profilePic}
                        alt={profilePic}
                        onError={e => { e.currentTarget.src = profilePic }}
                    />
                </div>
                <div
                    className="clap-name-container"
                >
                    {`${clap.user.firstName} ${clap.user.lastName}`}
                </div>
            </div>
        </div>
    )
}