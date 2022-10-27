import { useDispatch, useSelector } from "react-redux"

import Navbar from "../Navbar/Navbar"
import Header from "../Header/Header"
import LandingPostPreview from "./LandingPostPreview/LandingPostPreview"
import { isEmptyObj } from "../../utils/Objects"
import { readAllPostsThunk } from "../../store/posts"

import "./LandingPage.css"
import { useEffect } from "react"

export default function LandingPage() {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const posts = useSelector(state => state.posts.allPosts)

    const singlePost = useSelector(state => state.posts.singlePost)


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
            <div id="content-body-container">
                <div id="content-body-flex">
                    <div id="content-body">
                        <div id="content-posts-container">
                            {postArr.map(post => (
                                <LandingPostPreview post={post} />
                            ))}
                        </div>
                        <div id="content-sidebar-container">

                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}