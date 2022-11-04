const READ_POST_CLAPS = 'posts/READ_POST_CLAPS'

const readPostClaps = (claps) => ({
    type: READ_POST_CLAPS,
    claps
});

export const readPostClapsThunk = (postId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}/claps`);

    if (response.ok) {
        const claps = await response.json();
        dispatch(readPostClaps(claps))
        return null;
    } else {
        return response
    }
}

const initialState = {
    allClaps: {},
    singleClap: {}
}

export default function reducer(state = initialState, action) {
    let newState
    switch (action.type) {
        default:
            return state;
    }
}