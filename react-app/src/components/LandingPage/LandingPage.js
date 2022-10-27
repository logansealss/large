import { useDispatch, useSelector } from "react-redux"

import Navbar from "../Navbar/Navbar"
import Header from "../Header/Header"
import { isEmptyObj } from "../../utils/Objects"
import { readAllPostsThunk } from "../../store/posts"
import "./LandingPage.css"
import { useEffect } from "react"

export default function LandingPage() {

    const dispatch  = useDispatch()
    const user = useSelector(state => state.session.user)
    const posts = useSelector(state => state.posts.allPosts)

    useEffect(() => {

        dispatch(readAllPostsThunk())
    }, [])

    const postArr = Object.values(posts)

    return (
        <>
            <Navbar></Navbar>
            {isEmptyObj(user) && (
                <Header></Header>
            )} 
            {postArr.map(post => (
                <div key={post.id}>
                    {post.id}
                </div>
            ))}
        </>
    )
}