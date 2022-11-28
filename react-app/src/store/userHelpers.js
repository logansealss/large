import { readPostClaps } from "./claps";
import { readAllPosts, readSinglePost } from "./posts";
import { readPostResponses } from "./responses";
import { incrementFollowers, decrementFollowers, readUsers } from "./users"
import { setUser } from "./session"
import { 
    followUser, 
    unfollowUser, 
    readCurrentUserFollowing, 
    readCurrentUserFollowers 
} from "./follows";

export async function authenticate(dispatch) {
    const response = await fetch('/api/auth');

    if (response.ok) {
        const data = await response.json();
        if (data.errors) {
            return;
        }

        dispatch(setUser(data));
        dispatch(readUsers({ [data.id]: data }))
    }
}

export async function login(email, password, dispatch) {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password
        })
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(setUser(data))
        dispatch(readUsers({ [data.id]: data }))
        return null;
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ['An error occurred. Please try again.']
    }

}

export async function signUp(username, email, firstName, lastName, password, dispatch) {
    const response = await fetch('/api/auth/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            username,
            email,
            password,
        }),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(setUser(data))
        dispatch(readUsers({ [data.id]: data }))
        return null;
    } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ['An error occurred. Please try again.']
    }
}

export async function fetchAllPosts(dispatch) {
    const response = await fetch('/api/posts');

    if (response.ok) {
        const posts = await response.json();
        const postsForReducer = {}
        const usersForReducer = {}

        for (const post of Object.values(posts)) {
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

export async function fetchSinglePost(postId, dispatch) {
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

export async function fetchPostClaps(postId, dispatch) {
    const response = await fetch(`/api/posts/${postId}/claps`);

    if (response.ok) {
        const claps = await response.json();
        const clapsForReducer = {}
        const usersForReducer = {}

        for (const clap of Object.values(claps)) {
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

export async function fetchPostResponses(postId, dispatch) {
    const response = await fetch(`/api/posts/${postId}/responses`);

    if (response.ok) {
        const responses = await response.json();
        const responsesForReducer = {}
        const usersForReducer = {}

        for (const response of Object.values(responses)) {
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

export async function fetchFollowUser(userId, dispatch) {
    const response = await fetch(`/api/users/${userId}/follow`, {
        method: 'POST'
    });

    if (response.ok) {
        dispatch(followUser(userId))
        dispatch(incrementFollowers(userId))
        return null;
    } else {
        return response
    }
}

export async function fetchUnollowUser(userId, dispatch) {
    const response = await fetch(`/api/users/${userId}/follow`, {
        method: 'DELETE'
    });

    if (response.ok) {
        dispatch(unfollowUser(userId))
        dispatch(decrementFollowers(userId))
        return null;
    } else {
        return response
    }
}

export async function fetchUserFollowers(dispatch) {
    const response = await fetch(`/api/users/current/followers`);

    if (response.ok) {
        const followers = await response.json();
        const followersForReducer = {}
        const usersForReducer = {}

        for (const follower of Object.values(followers)) {
            usersForReducer[follower.id] = follower
            followersForReducer[follower.id] = follower.id
        }

        dispatch(readCurrentUserFollowers(followersForReducer))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}

export async function fetchUserFollowing(dispatch) {
    const response = await fetch(`/api/users/current/following`);

    if (response.ok) {
        const followers = await response.json();
        console.log(followers)
        const followersForReducer = {}
        const usersForReducer = {}

        for (const follower of Object.values(followers)) {
            usersForReducer[follower.id] = follower
            followersForReducer[follower.id] = follower.id
        }

        dispatch(readCurrentUserFollowing(followersForReducer))
        dispatch(readUsers(usersForReducer))
        return null;
    } else {
        return response
    }
}