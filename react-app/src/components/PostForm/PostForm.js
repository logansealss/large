import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom'
import { createPostThunk, updatePostThunk } from '../../store/posts';

import "./PostForm.css"

const PostForm = ({ postToUpdate }) => {

    let prevTitle
    let prevSubtitle
    let prevImageUrl
    let prevPost

    if (postToUpdate) {
        console.log("post to update", postToUpdate)
        prevTitle = postToUpdate.title
        prevPost = postToUpdate.post

        if (postToUpdate.subtitle) {
            prevSubtitle = postToUpdate.subtitle
        }
        if (postToUpdate.imageURL) {
            prevImageUrl = postToUpdate.imageURL
        }
    }

    const dispatch = useDispatch();
    const history = useHistory()
    const user = useSelector(state => state.session.user)

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

    if (!user) {
        return <Redirect to="/"></Redirect>
    }

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

        if(result.id){
            history.push(`/posts/${result.id}`)
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
                                    placeholder='Subtitle (optional)'
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
                                    placeholder="Image URL (optional)"
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
