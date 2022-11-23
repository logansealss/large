
import { useSelector, useDispatch } from "react-redux"

import { followUserThunk, unfollowUserThunk } from "../../store/follows"
import profilePic from "../../images/ProfilePic.png"
import './UserCard.css'

export default function UserCard({ user, className, position }) {

    const dispatch = useDispatch()

    const loggedInUser = useSelector(state => state.session.user)
    const following = useSelector(state => state.follows.following)

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
                className={`${position} user-card-container`}
            >
                <div className='user-card-header'>
                    <div
                        className="profile-pic-small"
                    >
                        <img
                            src={user.imageURL || profilePic}
                            alt={profilePic}
                            onError={e => { e.currentTarget.src = profilePic }}
                        />
                    </div>
                    <div
                        className="user-card-name"
                    >
                        {`${user.firstName} ${user.lastName}`}
                    </div>
                </div>
                {user.about &&
                    <div
                        className="user-card-about"
                    >
                        {user.about}
                    </div>
                }
                <div className='user-card-footer'>
                    <div>
                        x Followers
                    </div>
                    {loggedInUser &&
                        (following[user.id] ?
                            <button
                                className="following user-follow-button"
                                onClick={() => dispatch(unfollowUserThunk(user.id))}
                            >
                                Following
                            </button>
                            :
                            <button
                                className="color-two user-follow-button"
                                onClick={() => dispatch(followUserThunk(user.id))}
                            >
                                Follow
                            </button>
                        )
                    }
                </div>
            </div>
        </div>
    )
}