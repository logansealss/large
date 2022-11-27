const READ_USERS = 'users/READ_USERS'

export const readUsers = (users) => ({
    type: READ_USERS,
    users
})

const initialState = {}

export default function reducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case READ_USERS:
            return { ...state, ...action.users}
        default:
            return state;
    }
}