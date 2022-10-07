import React, { useState } from 'react'
import { ModalTitle, Modal, Button } from 'react-bootstrap';
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

    const submitUser = async () => {

    }

  return (
    <div className="d-flex flex-column">
        <button className="btn btn-secondary mt-2" onClick={openModal}>Create User</button>
        <Modal show={open} onHide={closeModal}>
            <ModalHeader closeButton>
                <ModalTitle>Create User</ModalTitle>
            </ModalHeader> 
            <Modal.Body>
                <div className="create-user-inputs">
                    <label>Username</label>
                    <input onChange={(e) => setUserName(e.target.value)}></input>
                    <label>Password</label>
                    <input type="password" onChange={(e) => setPassword(e.target.value)}></input>
                    <label>Re-enter Password</label>
                    <input type="password" onChange={(e) => setSecondPassword(e.target.value)}></input>
                </div>
            </Modal.Body>            

            <Modal.Footer>
                <Button variant="secondary" size="lg">Submit</Button>
            </Modal.Footer>
            
        </Modal>
    </div>
  )
}
