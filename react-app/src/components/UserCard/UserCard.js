
import { useSelector } from "react-redux"

import profilePic from "../../images/ProfilePic.png"
import './UserCard.css'

export default function UserCard({ user, className }) {

    const loggedInUser = useSelector(state => state.session.user)

    return (
        <div
            className='user-name-card-container'
        >
            <div
                className={className}
            >
                {`${user.firstName} ${user.lastName}`}
            </div>
            <div
                className={'user-card-container'}
            >
                <div className='user-card-header'>
                    <div
                        className="profile-pic-small"
                    >
                        <img
                            src={profilePic}
                        />
                    </div>
                    <div>
                        {`${user.firstName} ${user.lastName}`}
                    </div>
                </div>
                {user.about &&
                    <div>
                        {user.about}
                    </div>
                }
                <div className='user-card-footer'>
                    <div>
                        {user.followerCount}
                    </div>
                    {loggedInUser &&
                        <button
                            className="color-two user-follow-button"
                        >
                            Follow
                        </button>
                    }
                </div>
            </div>
        </div>
    )
}