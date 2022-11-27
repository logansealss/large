import { readAllPosts, readSinglePost } from "./posts";
import { readUsers } from "./users"

export async function fetchAllPosts(dispatch){
    const response = await fetch('/api/posts');

    if (response.ok) {
        const posts = await response.json();
        const postsForReducer = {}
        const usersForReducer = {}

        for(const post of Object.values(posts)){
            const user = post.writer
            usersForReducer[user.id] = user
            delete post["writer"]
            post["userId"] = user.id
            postsForReducer[post.id] = post
        }

        dispatch(readAllPosts(postsForReducer))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}

export async function fetchSinglePost(postId, dispatch){
    const response = await fetch(`/api/posts/${postId}`);

    if (response.ok) {
        const post = await response.json();

        const usersForReducer = {}
        const user = post.writer

        delete post["writer"]
        post["userId"] = user.id
        usersForReducer[user.id] = user

        dispatch(readSinglePost(post))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}