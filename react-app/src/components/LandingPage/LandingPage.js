import { useSelector } from "react-redux"

import Navbar from "../Navbar/Navbar"
import Header from "../Header/Header"
import { isEmptyObj } from "../../utils/Objects"
import "./LandingPage.css"

export default function LandingPage() {

    const user = useSelector(state => state.session.user)

    return (
        <>
            <Navbar></Navbar>
            {isEmptyObj(user) && (
                <Header></Header>
            )}
        </>
    )
}