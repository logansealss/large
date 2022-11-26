
import "./LoadingIcon.css"
import iconImage from "../../images/LoadingIcon.gif"

export default function LoadingIcon() {

    return (
        <div
            className="loading-icon-flex"
        >
            <img
                src={iconImage}
            />
        </div>
    )
}