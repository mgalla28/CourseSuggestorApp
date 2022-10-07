import React, { useState } from 'react'
import { ModalTitle, Modal } from 'react-bootstrap';
import ModalHeader from 'react-bootstrap/esm/ModalHeader';

export default function CreateUserModal() {
    const [open, setOpen] = useState(false);
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [secondPassword, setSecondPassword] = useState('');
    function openModal() {
        setOpen(true);
    }

    function closeModal() {
        setOpen(false);
    }

  return (
    <div className="d-flex flex-column">
    <button className="btn btn-secondary mt-2" onClick={openModal}>Create User</button>
    <Modal show={open} onHide={closeModal}>
        <ModalHeader closeButton>
            <ModalTitle>Create User</ModalTitle>
            <Modal.Body>
                <label>Username</label>
                <input onChange={(e) => setUserName(e.target.value)}></input>
                <label>Password</label>
                <input type="password" onChange={(e) => setPassword(e.target.value)}></input>
                <label>Re-enter Password</label>
                <input type="password" onChange={(e) => setSecondPassword(e.target.value)}></input>
            </Modal.Body>            
        </ModalHeader>
    </Modal>

    </div>
  )
}
