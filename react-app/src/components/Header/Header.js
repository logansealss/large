import { useHistory } from "react-router-dom"

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
                            <button
                                id="header-button"
                                className="navbar-header-button"
                                onClick={() =>history.push('/signup')}
                            >
                                Start Reading
                            </button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    )
}