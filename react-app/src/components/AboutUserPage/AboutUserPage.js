import { useSelector } from 'react-redux'
import { Redirect, NavLink } from 'react-router-dom'


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
                activeClassName="selected"
                className={isActive =>"about-links" + (!isActive ? " unselected" : "")}
            >About</NavLink>
        </div >
    )
}