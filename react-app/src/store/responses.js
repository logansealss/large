const READ_POST_RESPONSES = 'posts/READ_POST_RESPONSES'

const readPostResponses = (responses) => ({
    type: READ_POST_RESPONSES,
    responses
});

export const readPostResponsesThunk = (postId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}/responses`);

    if (response.ok) {
        const responses = await response.json();
        dispatch(readPostResponses(responses))
        return null;
    } else {
        return response
    }
}

const initialState = {}

export default function reducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case READ_POST_RESPONSES:
            return { ...action.responses }
        default:
            return state;
    }
}