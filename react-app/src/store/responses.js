const READ_POST_RESPONSES = 'posts/READ_POST_RESPONSES'
const CREATE_POST_RESPONSE = 'posts/CREATE_POST_RESPONSE'
const UPDATE_POST_RESPONSE = 'posts/UPDATE_POST_RESPONSE'

const readPostResponses = (responses) => ({
    type: READ_POST_RESPONSES,
    responses
});

const createPostResponse = (response) => ({
    type: CREATE_POST_RESPONSE,
    response
});

const updatePostResponse = (response) => ({
    type: UPDATE_POST_RESPONSE,
    response
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

export const createPostResponseThunk = (postId, newResponse) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}/responses`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newResponse),
    });

    if (response.ok) {
        const newResponse = await response.json();
        dispatch(createPostResponse(newResponse))
        return null;
    } else {
        return response
    }
}

export const updatePostResponseThunk = (postId, newResponse) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}/responses`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newResponse),
    });

    if (response.ok) {
        const newResponse = await response.json();
        dispatch(updatePostResponse(newResponse))
        return null;
    } else {
        return response
    }
}

const initialState = {}

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case READ_POST_RESPONSES:
            return { ...action.responses }
        case CREATE_POST_RESPONSE:
            return { ...state, [action.response.id]: action.response }
        case UPDATE_POST_RESPONSE:
            return { ...state, [action.response.id]: action.response }
        default:
            return state;
    }
}