import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory, useParams } from "react-router-dom";
import { readSinglePostThunk } from "../../store/posts";
import { fetchSinglePost } from "../../store/userHelpers";
import { isEmptyObj } from "../../utils/Objects";
import LoadingIcon from "../LoadingIcon/LoadingIcon";

import PostForm from "./PostForm";

export default function UpdatePostWrapper() {

    const { postId } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()
    // const user = useSelector(state => state.session.user)
    const userId = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const post = useSelector(state => state.posts.singlePost)
    const [loaded, setLoaded] = useState(false)

    useEffect(() => {

        (async () => {
            // const res = await dispatch(readSinglePostThunk(postId))
            const res = await fetchSinglePost(postId, dispatch)
            if(res){
                history.push('/')
            }
            setLoaded(true)
        })()
    }, [postId])

    if (!userId) {
        return <Redirect to="/"></Redirect>
    }

    if(!loaded){
        return <LoadingIcon></LoadingIcon>
    }

    if (post.userId !== userId){
        return <Redirect to='/'></Redirect>
    }

    return <PostForm postToUpdate={post}></PostForm>
}