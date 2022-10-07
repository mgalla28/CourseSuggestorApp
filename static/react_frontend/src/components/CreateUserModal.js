import React, { useState } from 'react'
import { ModalTitle, Modal, Button } from 'react-bootstrap';
import ModalHeader from 'react-bootstrap/esm/ModalHeader';

export default function CreateUserModal() {
    const [open, setOpen] = useState(false);
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [secondPassword, setSecondPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    function openModal() {
        setOpen(true);
    }

    function closeModal() {
        setOpen(false);
    }

    const submitUser = async () => {
        if (userName === '')
            setErrorMessage('Username required');
        else if (password !== secondPassword)
            setErrorMessage('Passwords must be the same')
        else {
            const loginInfo = {userName, password}
            document.body.style.cursor='wait'
            const res = await fetch('/create_user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(loginInfo)
            });

            if (res.ok) {
                const data = await res.json()
                if ('username' in data) {
                    alert('success')                
                }
            }
            else {
                setErrorMessage('Unable to create account');
                document.body.style.cursor='initial';
            }
        }
    }



  return (
    <div className="d-flex flex-column">
        <button className="btn btn-secondary mt-2" onClick={openModal}>Create User</button>
        <Modal show={open} onHide={closeModal}>
            <ModalHeader closeButton>
                <ModalTitle>Create User</ModalTitle>
            </ModalHeader> 
            <Modal.Body>
                <div className="alert alert-danger" hidden={errorMessage === ''}>{errorMessage}</div>
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
                <Button variant="secondary" size="lg" onClick={submitUser}>Submit</Button>
            </Modal.Footer>
            
        </Modal>
    </div>
  )
}
