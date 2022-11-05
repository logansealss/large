import { useSelector } from "react-redux"

export default function Claps(){

    const claps = useSelector(state => state.claps)
    const numClaps = Object.values(claps).reduce((sum, cur) => sum += cur.amount, 0)

    return (
        <div
            id="response-modal-content"
        >
            <div
                id="response-modal-header"
            >
                {`${numClaps} claps from ${Object.values(claps).length} people`}
            </div>
            {Object.values(claps).map(clap => (
                <div>
                    {`${clap.user.firstName} ${clap.user.lastName}`}
                </div>
            ))}
        </div>
    )
}