import { useDispatch, useSelector } from "react-redux"

import Navbar from "../Navbar/Navbar"
import Header from "../Header/Header"
import { isEmptyObj } from "../../utils/Objects"
import { readAllPostsThunk } from "../../store/posts"
import { readSinglePostThunk } from "../../store/posts"
import { readUserPostsThunk } from "../../store/posts"
import "./LandingPage.css"
import { useEffect } from "react"

export default function LandingPage() {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const posts = useSelector(state => state.posts.allPosts)

    const singlePost = useSelector(state => state.posts.singlePost)
    const userPosts = useSelector(state => state.posts.userPosts)

    useEffect(() => {

        // dispatch(readAllPostsThunk())
        // dispatch(readSinglePostThunk(1))
        dispatch(readUserPostsThunk(1))
    }, [])

    const postArr = Object.values(posts)

    return (
        <>
            <Navbar></Navbar>
            {isEmptyObj(user) && (
                <Header></Header>
            )}
            {/* {postArr.map(post => (
                <div key={post.id}>
                    {post.id}
                </div>
            ))} */}
            {/* {!isEmptyObj(singlePost) && (
                <div>
                    {singlePost.post}
                </div>
            )} */}
            {Object.values(userPosts).map(post => (
                <div key={post.id}>
                    {post.id}
                </div>
            ))}
        </>
    )
}