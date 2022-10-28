import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom'
import { createPostThunk, deletePostThunk, updatePostThunk } from '../../store/posts';

import "./PostForm.css"

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
            setTitleError('Must be 100 characters or less')
        } else {
            setTitleError()
        }

    }, [title])

    useEffect(() => {
        if (subtitle.length > 100) {
            setSubtitleError('Must be 100 characters or less')
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
            setImageUrlError('Must be 255 characters or less')
        }
        else if (imageUrl.length && !(/.\.(gif|jpe?g|tiff?|png|webp|bmp)$/i).test(imageUrl)) {
            setImageUrlError('Invalid image extension')
        }
        else {
            setImageUrlError()
        }
    }, [imageUrl])

    const onSubmit = async (e) => {
        e.preventDefault();

        if (!submitted) {
            setSubmitted(true)
        }

        if (titleError || subtitleError || postError || imageUrlError) {
            return;
        }

        const postToSubmit = {
            post,
            title,
            subtitle,
            image_url: imageUrl
        }

        let result;

        if (postToUpdate) {
            result = await dispatch(updatePostThunk(postToUpdate.id, postToSubmit))
        } else {
            result = await dispatch(createPostThunk(postToSubmit))
        }

        if (result.id) {
            history.push('/')
            // history.push(`/posts/${result.id}}`)
        } else {
            setServerError('Something went wrong. Please try again.')
        }
    };

    async function deletePost(e){
        e.preventDefault()
        const result = await dispatch(deletePostThunk(postToUpdate.id))

        if(!result){
            history.push('/')
        }
    }

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
        <div id="form-body">
            <div id="form-body-flex">
                <div id="form-body-center">
                    <div
                        id="form-container"
                    >
                        <form
                            id='post-form'
                            onSubmit={onSubmit}
                        >
                            <div id="post-button-container">
                                {postToUpdate && 
                                    <button
                                        id='post-form-button'
                                        className='delete-button'
                                        onClick={deletePost}
                                    >
                                        Delete post
                                    </button>
                                }
                                <button
                                    id="post-form-button"
                                    className='color-two'
                                    type='submit'
                                >
                                    {postToUpdate ? 'Save and publish' : 'Publish'}
                                </button>
                            </div>
                            <div
                                id="title-input-container"
                                className='input-container'
                            >
                                <div className={submitted && titleError ? 'input-error active' : 'input-error inactive'}>
                                    <div>
                                        {submitted ? titleError : ''}
                                    </div>
                                </div>
                                <input
                                    id="post-form-title"
                                    type='text'
                                    name='title'
                                    onChange={updateTitle}
                                    value={title}
                                    placeholder='Title'
                                    autoComplete="off"
                                ></input>
                            </div>
                            <div
                                id="subtitle-input-container"
                                className='input-container'
                            >
                                <div className={submitted && subtitleError ? 'input-error active' : 'input-error inactive'}>
                                    <div>
                                        {submitted ? subtitleError : ''}
                                    </div>
                                </div>
                                <input
                                    id="post-form-subtitle"
                                    type='text'
                                    name='subtitle'
                                    onChange={updateSubtitle}
                                    value={subtitle}
                                    placeholder='Subtitle'
                                    autoComplete="off"
                                ></input>
                            </div>
                            <div
                                id="imageurl-input-container"
                                className='input-container'
                            >
                                <div className={submitted && imageUrlError ? 'input-error active' : 'input-error inactive'}>
                                    <div>
                                        {submitted ? imageUrlError : ''}
                                    </div>
                                </div>
                                <input
                                    type='text'
                                    name='imageUrl'
                                    onChange={updateImageUrl}
                                    value={imageUrl}
                                    placeholder="Image URL"
                                    autoComplete="off"
                                ></input>
                            </div>
                            <div
                                id="post-input-container"
                                className='input-container'
                            >
                                <div className={submitted && postError ? 'input-error active' : 'input-error inactive'}>
                                    <div>
                                        {submitted ? postError : ''}
                                    </div>
                                </div>
                                <textarea
                                    id="post-form-post"
                                    // type='textarea'
                                    name='post'
                                    onChange={updatePost}
                                    value={post}
                                    placeholder="Write your post..."
                                    autoComplete="off"
                                ></textarea>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default PostForm;
