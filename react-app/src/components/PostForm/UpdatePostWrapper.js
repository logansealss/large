import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory, useParams } from "react-router-dom";
import { readSinglePostThunk } from "../../store/posts";
import { isEmptyObj } from "../../utils/Objects";

import PostForm from "./PostForm";

export default function UpdatePostWrapper() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector(state => state.session.user)
    const post = useSelector(state => state.posts.singlePost)

    // TODO: ADD REDIRECTS TO 404 PAGE ON ERRORS

    useEffect(() => {

        (async () => {
            const res = await dispatch(readSinglePostThunk(postId))

            if(res){
                history.push('/')
            }
        })()
    }, [postId])

    if (!user) {
        return <Redirect to="/"></Redirect>
    }

    const postIsEmpty = isEmptyObj(post)

    if (postIsEmpty ||  post.id !== +postId) {
        return (
            <div>
                loading
            </div>
        )
    } else{
        if(post.writer.id !== user.id){
            return <Redirect to='/'></Redirect>
        }
    }

    return <PostForm postToUpdate={post}></PostForm>
}