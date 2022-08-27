import React from 'react';

const LogoutButton = () => {

    const logout = () => {
        window.localStorage.removeItem('USER');
        window.location.reload();
    }


    return (
        <button className="btn btn-secondary float-right" onClick={logout}>Logout</button>
    )
}

export default LogoutButton;