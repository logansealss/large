import { useDispatch, useSelector } from "react-redux"

import Navbar from "../Navbar/Navbar"
import Header from "../Header/Header"
import LandingPostPreview from "./LandingPostPreview/LandingPostPreview"
import { isEmptyObj } from "../../utils/Objects"
import { readAllPostsThunk } from "../../store/posts"

import "./LandingPage.css"
import { useEffect, useState } from "react"

export default function LandingPage() {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const posts = useSelector(state => state.posts.allPosts)
    const [loaded, setLoaded] = useState(false)

    useEffect(() => {
        (async () => {
            await dispatch(readAllPostsThunk())
            setLoaded(true)
        })()
    }, [])

    const postArr = Object.values(posts)

    if(!loaded){
        return null
    }

    return (
        <>
            {isEmptyObj(user) && (
                <Header></Header>
            )}
            <div id="content-body-container">
                <div id="content-body-flex">
                    <div id="content-body">
                        <div id="content-posts-container">
                            {postArr.map(post => (
                                <LandingPostPreview key={post.id} post={post} />
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