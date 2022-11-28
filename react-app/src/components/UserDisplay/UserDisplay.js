import { useDispatch, useSelector } from "react-redux"

import { fetchFollowUser, fetchUnfollowUser } from "../../store/userHelpers"
import "./UserDisplay.css"
import profilePic from "../../images/ProfilePic.png"

export default function UserDisplay({ user }) {

    const dispatch = useDispatch()
    const loggedInUserId = useSelector(state => state.session.user)
    const loggedInUser = useSelector(state => state.users[loggedInUserId])
    const following = useSelector(state => state.follows.following)

    return (
        <div
            className="user-display-container"
        >
            <div
                className="user-display-flex"
            >
                <div
                    className="user-display-data-flex"
                >
                    <div
                        className="user-display-image-container"
                    >
                        <img
                            src={user.imageURL || profilePic}
                            alt={profilePic}
                            onError={e => { e.currentTarget.src = profilePic }}
                        />
                    </div>
                    <div
                        className="user-data-flex"
                    >
                        <div
                            className="user-data-name"
                        >
                            {`${user.firstName} ${user.lastName}`}
                        </div>
                        <div
                            className="user-data-about"
                        >
                            {`${user.about}`}
                        </div>
                    </div>
                </div>
                <div>
                    {(following[user.id] ?
                        <button
                            className="following user-follow-button"
                            onClick={() => fetchUnfollowUser(user.id, dispatch)}
                        >
                            Following
                        </button>
                        :
                        <button
                            className="color-two user-follow-button"
                            onClick={() => fetchFollowUser(user.id, dispatch)}
                        >
                            Follow
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}