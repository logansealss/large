const READ_CURRENT_USER_FOLLOWERS = 'follows/READ_CURRENT_USER_FOLLOWERS'
const READ_CURRENT_USER_FOLLOWING = 'follows/READ_CURRENT_USER_FOLLOWING'

const readCurrentUserFollowers = (followers) => ({
    type: READ_CURRENT_USER_FOLLOWERS,
    followers
})

const readCurrentUserFollowing = (following) => ({
    type: READ_CURRENT_USER_FOLLOWING,
    following
})

export const readCurrentUserFollowersThunk = () => async (dispatch) => {
    const response = await fetch(`/api/follows/current`);

    if (response.ok) {
        const follows = await response.json();
        dispatch(readCurrentUserFollowers(follows))
        return null;
    } else {
        return response
    }
}

export const readCurrentUserFollowingThunk = () => async (dispatch) => {
    const response = await fetch(`/api/follows/current`);

    if (response.ok) {
        const follows = await response.json();
        dispatch(readCurrentUserFollowers(follows))
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
    let newState
    switch (action.type) {
        case READ_CURRENT_USER_FOLLOWERS:
            return {
                following: {...state.following},
                followers: {...action.followers}
            }
        default:
            return state;
    }
}