// constants
const READ_ALL_POSTS = 'posts/READ_ALL_POSTS';

const readAllPosts = (posts) => ({
    type: READ_ALL_POSTS,
    posts
});

export const readAllPostsThunk = () => async (dispatch) => {
    const response = await fetch('/api/posts');

    if (response.ok) {
        const posts = await response.json();
        dispatch(readAllPosts(posts))
        return null;
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return response
    }

}

const initialState = {
    allPosts: {},
    singlePost: {},
    userPosts: {}
}

export default function reducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case READ_ALL_POSTS:
            return { ...state, allPosts: action.posts }
        default:
            return state;
    }
}