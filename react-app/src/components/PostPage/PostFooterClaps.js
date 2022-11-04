
import { useSelector } from "react-redux"

import ReusableModal from "../../context/ReusableModal"
import clap from "../../images/clap.svg"
import Claps from "./Claps/Claps"

export default function PostFooterClaps() {

    const claps = useSelector(state => state.claps)

    const numClaps = Object.values(claps).reduce((sum, cur) => sum += cur.amount, 0)

    return (
        <div id="post-footer-claps">
            <div id="post-footer-claps-flex">
                <div className="svg-container svg-claps">
                    <img src={clap} />
                </div>
                {!!numClaps &&
                    (<ReusableModal
                        container={
                            <div>
                                {numClaps}
                            </div>
                        }
                        bgClass='responses-modal-background'
                    >
                        <Claps></Claps>
                    </ReusableModal>
                    )
                }
                {!numClaps &&
                    <div>
                        --
                    </div>
                }
            </div>
        </div>
    )
}