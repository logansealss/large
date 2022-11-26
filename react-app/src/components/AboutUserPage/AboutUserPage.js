import { useSelector } from 'react-redux'
import { Redirect, NavLink, use, Switch, Route } from 'react-router-dom'

import "./AboutUserPage.css"
import UserProfileImage from './UserProfileImage/UserProfileImage'

export function AboutUserPage() {

    const user = useSelector(state => state.session.user)

    if (!user) {
        return <Redirect to="/"></Redirect>
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
                        >About</NavLink>
                        <NavLink
                            to="/about/posts"
                            activeClassName="selected"
                            className='about-link'
                        >Posts</NavLink>
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
                        <Route exact path="/about/posts">
                            <div>
                                these are the posts
                            </div>
                        </Route>
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
                                <UserProfileImage></UserProfileImage>
                            </div>
                        </Route>
                    </Switch>
                </div >
            </div>
        </div>
    )
}