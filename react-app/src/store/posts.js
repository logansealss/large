// constants
const READ_ALL_POSTS = 'posts/READ_ALL_POSTS';
const READ_SINGLE_POST = 'posts/READ_SINGLE_POST'
const READ_USER_POSTS = 'posts/READ_USER_POSTS'
const CREATE_POST = 'posts/CREATE_POST'

const readAllPosts = (posts) => ({
    type: READ_ALL_POSTS,
    posts
});

const readSinglePost = (post) => ({
    type: READ_SINGLE_POST,
    post
});

const readUserPosts = (posts) => ({
    type: READ_USER_POSTS,
    posts
});

const createPost = (post) => ({
    type: CREATE_POST,
    post
});

export const readAllPostsThunk = () => async (dispatch) => {
    const response = await fetch('/api/posts');

    if (response.ok) {
        const posts = await response.json();
        dispatch(readAllPosts(posts))
        return null;
    } else {
        return response
    }
}

export const readSinglePostThunk = (postId) => async (dispatch) => {
    const response = await fetch(`/api/posts/${postId}`);

    if (response.ok) {
        const post = await response.json();
        dispatch(readSinglePost(post))
        return null;
    } else {
        return response
    }
}

export const readUserPostsThunk = (writerId) => async (dispatch) => {
    const response = await fetch(`/api/users/${writerId}/posts`);

    if (response.ok) {
        const userPosts = await response.json();
        dispatch(readUserPosts(userPosts))
        return null;
    } else {
        return response
    }
}

export const createPostThunk = (post, user) => async (dispatch) => {
    const response = await fetch('/api/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(post),
    });

    if (response.ok) {
        const newPost = await response.json();
        dispatch(createPost(newPost));
        return newPost;
    } else {
        return response;
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
        case READ_SINGLE_POST:
            return { ...state, singlePost: action.post }
        case READ_USER_POSTS:
            return { ...state, userPosts: action.posts }
        case CREATE_POST:
            const newPost = action
            return { ...state,  }
        default:
            return state;
    }
}