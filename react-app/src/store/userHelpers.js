import { readPostClaps } from "./claps";
import { readAllPosts, readSinglePost } from "./posts";
import { readPostResponses } from "./responses";
import { readUsers } from "./users"
import { setUser } from "./session"

export async function authenticate(dispatch){
    const response = await fetch('/api/auth');

      if (response.ok) {
        const data = await response.json();
        if (data.errors) {
          return;
        }
      
        dispatch(setUser(data));
        dispatch(readUsers({ [data.id]: data}))
      }
}

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

export async function fetchPostClaps(postId, dispatch){
    const response = await fetch(`/api/posts/${postId}/claps`);

    if (response.ok) {
        const claps = await response.json();
        const clapsForReducer = {}
        const usersForReducer = {}

        for(const clap of Object.values(claps)){
            const user = clap.user
            usersForReducer[user.id] = user
            delete clap["user"]
            clap["userId"] = user.id
            clapsForReducer[clap.id] = clap
        }

        dispatch(readPostClaps(clapsForReducer))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}

export async function fetchPostResponses(postId, dispatch){
    const response = await fetch(`/api/posts/${postId}/responses`);

    if (response.ok) {
        const responses = await response.json();
        const responsesForReducer = {}
        const usersForReducer = {}

        for(const response of Object.values(responses)){
            const user = response.user
            usersForReducer[user.id] = user
            delete response["user"]
            response["userId"] = user.id
            responsesForReducer[response.id] = response
        }

        dispatch(readPostResponses(responsesForReducer))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}