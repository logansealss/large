import { useHistory } from "react-router-dom"

import ReusableModal from '../../context/ReusableModal'
import SignupForm from '../auth/SignUpForm'
import "./Header.css"

export default function Header() {

    const history = useHistory()

    return (
        <div
            id="header"
            className="bottom-border"
        >
            <div id="header-flex">
                <div id="header-flex-buffer">
                    <div id="header-content-flex">
                        <div id="header-content">
                            <div
                                id="header-heading"
                            >
                                Stay curious.
                            </div>
                            <div
                                id="header-body"
                            >
                                Discover stories, thinking, and expertise from writers on any topic.
                            </div>
                            <ReusableModal
                                displayText='Get started'
                                container={
                                    (<button
                                        id="header-button"
                                        className="navbar-header-button"
                                    >
                                        Start Reading
                                    </button>
                                    )
                                }
                            >
                                <SignupForm></SignupForm>
                            </ReusableModal>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}