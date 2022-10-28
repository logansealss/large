import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { Modal } from './Modal';

function ReusableModal({ container, children, afterClick }) {
    const [showModal, setShowModal] = useState(false);

    const user = useSelector(state => state.session.user)

    function onClose() {
        setShowModal(false);
    }

    function modOnClick(e){
        setShowModal(cur => !cur)
        afterClick && afterClick()
    }

    return (
        <>
            {React.cloneElement(container, {
                onClick: modOnClick
            })}
            {showModal && (
                <Modal
                    onClose={() => setShowModal(false)}
                >
                    {React.cloneElement(children, {
                        onClose: onClose
                    })}
                </Modal>
            )}
        </>
    );
}

export default ReusableModal;