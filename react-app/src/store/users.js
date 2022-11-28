const READ_USERS = 'users/READ_USERS'
const INCREMENT_USER_FOLLOWERS = 'users/INCREMENT_USER_FOLLOWERS'
const DECREMENT_USER_FOLLOWERS = 'users/DECREMENT_USER_FOLLOWERS'


export const readUsers = (users) => ({
    type: READ_USERS,
    users
})

export const incrementFollowers = userId => ({
    type: INCREMENT_USER_FOLLOWERS,
    userId
})

export const decrementFollowers = userId => ({
    type: DECREMENT_USER_FOLLOWERS,
    userId
})

const initialState = {}

export default function reducer(state = initialState, action) {
    let updatedUser
    switch (action.type) {
        case READ_USERS:
            return { ...state, ...action.users }
        case INCREMENT_USER_FOLLOWERS:
            updatedUser = { ...state[action.userId] }
            updatedUser.followerCount++
            return { ...state, [action.userId]: { ...updatedUser } }
        case DECREMENT_USER_FOLLOWERS:
            updatedUser = { ...state[action.userId] }
            updatedUser.followerCount--
            return { ...state, [action.userId]: { ...updatedUser } }
        default:
            return state;
    }
}