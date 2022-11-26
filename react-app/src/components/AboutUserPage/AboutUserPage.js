import { useSelector, useDispatch } from 'react-redux'
import { Redirect, NavLink, Switch, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'

import { readCurrentUserPostsThunk } from '../../store/posts'
import AboutUserProfile from './AboutUserProfile/AboutUserProfile'
import AltPostDisplay from '../AltPostDisplay/AltPostDisplay'
import "./AboutUserPage.css"

// TODO: add route to view and update user profile

export function AboutUserPage() {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const userPosts = useSelector(state => state.posts.allPosts)
    const [loaded, setLoaded] = useState(false)

    useEffect(() => {
        (async () => {
            await dispatch(readCurrentUserPostsThunk())
            setLoaded(true)
        })()
    }, [])

    if (!user) {
        return <Redirect to="/"></Redirect>
    }

    if(!loaded){
        return null
    }

    return (
        <div
            className='about-container'
        >
            <div
                className='about-container-flex'
            >
                <div
                    className='about-content-container'
                >

                    <div
                        className='about-name'
                    >
                        {`${user.firstName} ${user.lastName}`}
                    </div>
                    <div
                        className='about-links-container'
                    >
                        <NavLink
                            to="/about"
                            exact={true}
                            activeClassName="selected"
                            className='about-link'
                        >Home</NavLink>
                        {/* <NavLink
                            to="/about/posts"
                            activeClassName="selected"
                            className='about-link'
                        >Posts</NavLink> */}
                        <NavLink
                            to="/about/following"
                            activeClassName="selected"
                            className='about-link'
                        >Following</NavLink>
                        <NavLink
                            to="/about/followers"
                            activeClassName="selected"
                            className='about-link'
                        >Followers</NavLink>
                    </div>
                    <Switch>
                        {/* <Route exact path="/about/posts">
                            <div>
                                these are the posts
                            </div>
                        </Route> */}
                        <Route exact path="/about/following">
                            <div>
                                folowing these people
                            </div>
                        </Route>
                        <Route exact path="/about/followers">
                            <div>
                                these people following you
                            </div>
                        </Route>
                        <Route exact path="/about">
                            <div>
                                {Object.values(userPosts).map(post => 
                                    <AltPostDisplay
                                        post={post}
                                        key={post.id}
                                    >
                                    </AltPostDisplay>)}
                                {Object.values(userPosts).length === 0 && 
                                    <div>
                                        No posts to show.
                                    </div>
                                }
                            </div>
                            {/* <div>
                                <AboutUserProfile></AboutUserProfile>
                            </div> */}
                        </Route>
                    </Switch>
                </div >
            </div>
        </div>
    )
}