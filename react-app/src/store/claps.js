const READ_POST_CLAPS = 'claps/READ_POST_CLAPS'
const CREATE_POST_CLAP = 'claps/CREATE_POST_CLAP'
const UPDATE_POST_CLAP = 'claps/UPDATE_POST_CLAP'
const DELETE_POST_CLAP = 'claps/DELETE_POST_CLAP'

const readPostClaps = (claps) => ({
    type: READ_POST_CLAPS,
    claps
});

const createPostClap = (clap) => ({
    type: CREATE_POST_CLAP,
    clap
});

const updatePostClap = (clap) => ({
    type: UPDATE_POST_CLAP,
    clap
});

const deletePostClap = (id) => ({
    type: DELETE_POST_CLAP,
    id
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

export const createPostClapThunk = (postId, newClap) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}/claps`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newClap),
    });

    if (response.ok) {
        const newClap = await response.json();
        dispatch(createPostClap(newClap))
        return null;
    } else {
        return response
    }
}

export const updatePostClapThunk = (clapId, newClap) => async (dispatch) => {
    const response = await fetch(`/api/claps/${clapId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newClap),
    });

    if (response.ok) {
        const newClap = await response.json();
        dispatch(updatePostClap(newClap))
        return null;
    } else {
        return response
    }
}

export const deletePostClapThunk = (clapId) => async (dispatch) => {
    const response = await fetch(`/api/claps/${clapId}`, {
        method: 'DELETE',
    });

    if (response.ok) {
        dispatch(deletePostClap(clapId))
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
    let allClaps
    let singleClap
    switch (action.type) {
        case READ_POST_CLAPS:
            return {
                ...state,
                allClaps: { ...action.claps }
            }
        case CREATE_POST_CLAP:
            return {
                allClaps: { ...state.allClaps, [action.clap.id]: action.clap },
                singleClap: { ...action.clap }
            }
        case UPDATE_POST_CLAP:
            return {
                allClaps: { ...state.allClaps, [action.clap.id]: action.clap },
                singleClap: { ...action.clap }
            }
        case DELETE_POST_CLAP:
            allClaps = { ...state.allClaps }
            delete allClaps[action.id]
            singleClap = { ...state.singleClap }
            if(singleClap.id && singleClap.id === action.id){
                singleClap = {}
            }
            return { allClaps, singleClap }
        default:
            return state;
    }
}