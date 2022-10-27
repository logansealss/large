
import "./Header.css"

export default function Header() {

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
                                <span>

                                    Stay curious.
                                </span>
                            </div>
                            <div
                                id="header-body"
                            >
                                Discover stories, thinking, and expertise from writers on any topic.
                            </div>
                            <button
                                id="header-button"
                                className="navbar-header-button"
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