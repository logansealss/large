import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom'
import { createPostThunk } from '../../../store/posts';



const PostForm = ({ postToUpdate }) => {

    let prevTitle
    let prevSubtitle
    let prevImageUrl
    let prevPost

    if (postToUpdate) {
        prevTitle = postToUpdate.title
        prevPost = postToUpdate.post

        if (postToUpdate.prevSubtitle) {
            prevSubtitle = postToUpdate.prevSubtitle
        }
        if (postToUpdate.prevImageUrl) {
            prevImageUrl = postToUpdate.prevImageUrl
        }
    }

    const dispatch = useDispatch();
    const history = useHistory()

    const [serverError, setServerError] = useState();
    const [titleError, setTitleError] = useState();
    const [subtitleError, setSubtitleError] = useState();
    const [imageUrlError, setImageUrlError] = useState();
    const [postError, setPostError] = useState();

    const [title, setTitle] = useState(prevTitle || '');
    const [subtitle, setSubtitle] = useState(prevSubtitle || '');
    const [imageUrl, setImageUrl] = useState(prevImageUrl || '');
    const [post, setPost] = useState(prevPost || '');

    const [submitted, setSubmitted] = useState(false)

    useEffect(() => {
        if (title.length === 0) {
            setTitleError('Title is required')
        } else if (title.length > 100) {
            setTitleError('Title must be 100 characters or less')
        } else {
            setTitleError()
        }

    }, [title])

    useEffect(() => {
        if (subtitle.length > 100) {
            setSubtitleError('Subtitle must be 100 characters or less')
        } else {
            setSubtitleError()
        }
    }, [subtitle])

    useEffect(() => {
        if (post.length === 0) {
            setPostError('Post is required')
        } else {
            setPostError()
        }
    }, [post])

    useEffect(() => {
        if (imageUrl.length > 255) {
            setImageUrlError('Image URL must be 255 characters or less')
        }
        // else if () {
        //     setImageUrlError('Image URL must be 255 characters or less')
        // }
        else {
            setImageUrlError()
        }
    }, [imageUrl])

    const onSubmit = async (e) => {
        e.preventDefault();

        if (!submitted) {
            setSubmitted(true)
        }

        if(titleError || subtitleError || postError || imageUrlError){
            return;
        }

        const postToSubmit = {
            post,
            title,
            subtitle,
            image_url: imageUrl
        }

        const result = await dispatch(createPostThunk(postToSubmit))

        if (result.id) {
            // history.push(`/posts/${result.id}}`)
            console.log("the new post: ", result)
        } else {
            setServerError('Something went wrong. Please try again.')
        }
    };


    const updateTitle = (e) => {
        setTitle(e.target.value);
    };

    const updateSubtitle = (e) => {
        setSubtitle(e.target.value);
    };

    const updateImageUrl = (e) => {
        setImageUrl(e.target.value);
    };

    const updatePost = (e) => {
        setPost(e.target.value);
    };

    return (
        <form onSubmit={onSubmit}>
            {submitted && titleError && (
                <div>
                    {titleError}
                </div>
            )}
            <div>
                <label>Title</label>
                <input
                    type='text'
                    name='title'
                    onChange={updateTitle}
                    value={title}
                    placeholder='Title'
                ></input>
            </div>
            {submitted && subtitleError && (
                <div>
                    {subtitleError}
                </div>
            )}
            <div>
                <label>Subtitle</label>
                <input
                    type='text'
                    name='subtitle'
                    onChange={updateSubtitle}
                    value={subtitle}
                    placeholder="Subtitle"
                ></input>
            </div>
            {submitted && postError && (
                <div>
                    {postError}
                </div>
            )}
            <div>
                <label>Post</label>
                <input
                    type='text'
                    name='post'
                    onChange={updatePost}
                    value={post}
                    placeholder="Write your post..."
                ></input>
            </div>
            {submitted && imageUrlError && (
                <div>
                    {imageUrlError}
                </div>
            )}
            <div>
                <label>Post Image</label>
                <input
                    type='text'
                    name='imageUrl'
                    onChange={updateImageUrl}
                    value={imageUrl}
                    placeholder="Image URL"
                ></input>
            </div>
            <button
                type='submit'
            >Publish</button>
        </form>
    );
};

export default PostForm;
