
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"

import { createPostClapThunk, updatePostClapThunk } from "../../store/claps"
import ReusableModal from "../../context/ReusableModal"
import sparkles from "../../images/sparkles.svg"
import clap from "../../images/clap.svg"
import Claps from "./Claps/Claps"

export default function PostFooterClaps() {

    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const claps = useSelector(state => state.claps)
    const post = useSelector(state => state.posts.singlePost)
    const numClaps = Object.values(claps).reduce((sum, cur) => sum += cur.amount, 0)

    let userClap
    if (user) {
        userClap = Object.values(claps).find(clap => clap.user.id === user.id)
    }

    const [intObj, setIntObj] = useState()
    const [timeoutObj, setTimeoutObj] = useState()
    const [clapsAmount, setClapsAmount] = useState(userClap ? userClap.amount : 0)
    const [bubbleVisible, setBubbleVisible] = useState(false)

    useEffect(() => {

        let userClap
        if(user){
            userClap = Object.values(claps).find(clap => clap.user.id === user.id)
        }
        setClapsAmount(userClap ? userClap.amount : 0)
    }, [user, claps])

    async function bubbleDisappears() {

        const clapsToSend = clapsAmount > 50 ? 50 : clapsAmount

        if (userClap) {
            await dispatch(updatePostClapThunk(userClap.id, { amount: clapsToSend }))
        }
        else {
            await dispatch(createPostClapThunk(post.id, { amount: clapsToSend }))
        }
        console.log("clap created/updated")
        setBubbleVisible(false)
    }

    function clapsCounter() {

        if (clapsAmount < 50) {
            setClapsAmount(cur => cur + 1)
        }
    }

    function clapsStopClick() {

        if (intObj) {
            clearInterval(intObj)
            setIntObj()
        }
        setTimeoutObj(setTimeout(bubbleDisappears, 750))
    }

    function clapsMouseDown() {
        if (timeoutObj) {
            clearTimeout(timeoutObj)
        }
        if (clapsAmount < 50) {
            setClapsAmount(cur => cur + 1)
            setIntObj(setInterval(clapsCounter, 350))
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
                        className={user && user.id !==post.writer.id ? "svg-container svg-claps hover" : "svg-container svg-claps"}
                        onMouseDown={user && user.id !==post.writer.id ? clapsMouseDown : undefined}
                        onMouseUp={user && user.id !==post.writer.id ? clapsStopClick : undefined}
                        onDragEnd={user && user.id !==post.writer.id ? clapsStopClick : undefined}
                    >
                        <img src={clap} />
                    </div>
                    <div
                        className={bubbleVisible ? "floating-claps visible" : "floating-claps hidden"}
                    >
                        <div>
                            {clapsAmount <= 50 ? clapsAmount : 50}
                        </div>
                    </div>
                    <div
                        className={bubbleVisible ? "floating-sparkles-right visible" : "floating-sparkles-right hidden"}
                    >
                        <img src={sparkles} />
                    </div>
                    <div
                        className={bubbleVisible ? "floating-sparkles-left visible" : "floating-sparkles-left hidden"}
                    >
                        <img src={sparkles} />
                    </div>
                </div>
                {!!numClaps &&
                    (<ReusableModal
                        container={
                            <div
                                className="total-claps-div"
                            >
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