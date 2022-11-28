import { useSelector, useDispatch } from 'react-redux'
import { Redirect, NavLink, Switch, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'

import { readCurrentUserPostsThunk } from '../../store/posts'
import { fetchUserFollowers } from '../../store/userHelpers'
import LoadingIcon from '../LoadingIcon/LoadingIcon'
import UserDisplay from '../UserDisplay/UserDisplay'
import AboutUserProfile from './AboutUserProfile/AboutUserProfile'
import AltPostDisplay from '../AltPostDisplay/AltPostDisplay'
import "./AboutUserPage.css"

// TODO: add route to view and update user profile

export function AboutUserPage() {

    const dispatch = useDispatch()
    const userId = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const userPosts = useSelector(state => state.posts.allPosts)
    const followers = useSelector(state => state.follows.followers)
    const following = useSelector(state => state.follows.following)
    const users = useSelector(state => state.users)
    const [loaded, setLoaded] = useState(false)

    useEffect(() => {
        (async () => {
            await dispatch(readCurrentUserPostsThunk())
            await fetchUserFollowers(dispatch)
            setLoaded(true)
        })()
    }, [])

    if (!user) {
        return <Redirect to="/"></Redirect>
    }

    if (!loaded) {
        return (
            <LoadingIcon />
        )
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
                                {Object.values(following).map(userId =>
                                    <UserDisplay
                                        user={users[userId]}
                                        key={userId}
                                    />)
                                }
                                {Object.values(following).length === 0 &&
                                    <div>
                                        You're not following anyone yet.
                                    </div>
                                }
                            </div>
                        </Route>
                        <Route exact path="/about/followers">
                            <div>
                                {Object.values(followers).map(userId =>
                                    <UserDisplay
                                        user={users[userId]}
                                        key={userId}
                                    />)
                                }
                                {Object.values(followers).length === 0 &&
                                    <div>
                                        You don't have any followers yet.
                                    </div>
                                }
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
                                        You don't have any posts yet.
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