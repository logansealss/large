
import { useSelector } from "react-redux"
import { useState } from "react"

import ReusableModal from "../../context/ReusableModal"
import clap from "../../images/clap.svg"
import Claps from "./Claps/Claps"

export default function PostFooterClaps() {

    const user = useSelector(state => state.session.user)
    const claps = useSelector(state => state.claps)
    const numClaps = Object.values(claps).reduce((sum, cur) => sum += cur.amount, 0)
    const [intObj, setIntObj] = useState()
    const [timeoutObj, setTimeoutObj] = useState()
    const [clapsAmount, setClapsAmount] = useState(0)
    const [bubbleVisible, setBubbleVisible] = useState(false)

    function bubbleDisappears(){
        setBubbleVisible(false)
        
    }

    function clapsCounter() {

        if(clapsAmount < 50){
            setClapsAmount(cur => cur + 1)
        }
    }

    function clapsStopClick() {

        if(intObj){
            clearInterval(intObj)
            setIntObj()
        }
        setTimeoutObj(setTimeout(bubbleDisappears, 750))
    }

    function clapsMouseDown() {
        if(timeoutObj){
            clearTimeout(timeoutObj)
        }
        if(clapsAmount < 50){
            setClapsAmount(cur => cur + 1)
            setIntObj(setInterval(clapsCounter, 500))
        }
        setBubbleVisible(true)
    }

    return (
        <div id="post-footer-claps">
            <div id="post-footer-claps-flex">
                <div
                    className="claps-container"
                >
                    <div
                        className="svg-container svg-claps"
                        onMouseDown={clapsMouseDown}
                        onMouseUp={clapsStopClick}
                        onDragEnd={clapsStopClick}
                    >
                        <img src={clap} />
                    </div>
                    <div
                        className={bubbleVisible? "floating-claps visible" : "floating-claps hidden"}
                    >
                        <div>
                            {clapsAmount <= 50 ? clapsAmount : 50}
                        </div>
                    </div>
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