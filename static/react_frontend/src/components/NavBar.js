import React from 'react';
import LogoutButton from './LogoutButton'

function NavBar(props) {
    return (
        <nav className='navbar navbar-expand-lg justify-content-between Navbar'>
            <button className='nav-link float-left'>{props.userName}</button>
            <LogoutButton />
        </nav>
    )
}

export default NavBar;