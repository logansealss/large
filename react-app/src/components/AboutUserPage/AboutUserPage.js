import { useSelector } from 'react-redux'
import { Redirect, NavLink, use, Switch, Route } from 'react-router-dom'


import "./AboutUserPage.css"

export function AboutUserPage() {

    const user = useSelector(state => state.session.user)

    if (!user) {
        return <Redirect to="/"></Redirect>
    }

    return (
        <div

        >
            <div>
                {`${user.firstName} ${user.lastName}`}
            </div>
            <NavLink
                to="/about"
                exact={true}
                activeClassName="selected"
                className={isActive => "about-links" + (!isActive ? " unselected" : "")}
            >About</NavLink>
            <NavLink
                to="/about/posts"
                activeClassName="selected"
                className={isActive => "about-links" + (!isActive ? " unselected" : "")}
            >Posts</NavLink>
            <NavLink
                to="/about/following"
                activeClassName="selected"
                className={isActive => "about-links" + (!isActive ? " unselected" : "")}
            >Following</NavLink>
            <NavLink
                to="/about/followers"
                activeClassName="selected"
                className={isActive => "about-links" + (!isActive ? " unselected" : "")}
            >Followers</NavLink>
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
                        about
                    </div>
                </Route>
            </Switch>
        </div >
    )
}