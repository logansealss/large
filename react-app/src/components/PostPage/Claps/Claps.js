import { useSelector } from "react-redux"
import Clap from "./Clap"

export default function Claps(){

    const claps = useSelector(state => state.claps)
    const users = useSelector(state => state.users)
    const numClaps = Object.values(claps).reduce((sum, cur) => sum += cur.amount, 0)

    return (
        <div
            id="response-modal-content"
        >
            <div
                id="response-modal-header"
            >
                {`${numClaps} claps from ${Object.values(claps).length} ${Object.values(claps).length === 1 ? 'person' : 'people'}`}
            </div>
            <div
                className="response-form-bottom-border"
            ></div>
            {Object.values(claps).map(clap => (
                <Clap
                    clap={clap}
                    user={users[clap.userId]}
                    key={clap.id}
                >
                </Clap>
            ))}
        </div>
    )
}