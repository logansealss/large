const READ_CURRENT_USER_FOLLOWERS = 'follows/READ_CURRENT_USER_FOLLOWERS'
const READ_CURRENT_USER_FOLLOWING = 'follows/READ_CURRENT_USER_FOLLOWING'
const FOLLOW_USER = 'follows/FOLLOW_USER'
const UNFOLLOW_USER = 'follows/UNFOLLOW_USER'
const CLEAR_FOLLOWS = 'follows/CLEAR_FOLLOWS'

const readCurrentUserFollowers = (followers) => ({
    type: READ_CURRENT_USER_FOLLOWERS,
    followers
})

const readCurrentUserFollowing = (following) => ({
    type: READ_CURRENT_USER_FOLLOWING,
    following
})

const followUser = (userId) => ({
    type: FOLLOW_USER,
    userId
})

const unfollowUser = (userId) => ({
    type: UNFOLLOW_USER,
    userId
})

export const clearFollows = () => ({
    type: CLEAR_FOLLOWS
})

export const readCurrentUserFollowersThunk = () => async (dispatch) => {
    const response = await fetch(`/api/users/current/followers`);

    if (response.ok) {
        const followers = await response.json();
        dispatch(readCurrentUserFollowers(followers))
        return null;
    } else {
        return response
    }
}

export const readCurrentUserFollowingThunk = () => async (dispatch) => {
    const response = await fetch(`/api/users/current/following`);

    if (response.ok) {
        const following = await response.json();
        dispatch(readCurrentUserFollowing(following))
        return null;
    } else {
        return response
    }
}

export const followUserThunk = (userId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}/follow`, {
        method: 'POST'
    }
    );

    if (response.ok) {
        dispatch(followUser(userId))
        return null;
    } else {
        return response
    }
}

export const unfollowUserThunk = (userId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}/follow`, {
        method: 'DELETE'
    }
    );

    if (response.ok) {
        dispatch(unfollowUser(userId))
        return null;
    } else {
        return response
    }
}

const initialState = {
    followers: {},
    following: {}
}

export default function reducer(state = initialState, action) {
    let newFollowing
    switch (action.type) {
        case READ_CURRENT_USER_FOLLOWERS:
            return {
                following: { ...state.following },
                followers: { ...action.followers }
            }
        case READ_CURRENT_USER_FOLLOWING:
            return {
                followers: { ...state.followers },
                following: { ...action.following }
            }
        case FOLLOW_USER:
            return {
                ...state,
                following: { ...state.following, [action.userId]: action.userId }
            }
        case UNFOLLOW_USER:
            newFollowing = { ...state.following }
            delete newFollowing[action.userId]
            return {
                ...state,
                following: newFollowing
            }
        case CLEAR_FOLLOWS:
            return {
                followers: {},
                following: {}
            }
        default:
            return state;
    }
}