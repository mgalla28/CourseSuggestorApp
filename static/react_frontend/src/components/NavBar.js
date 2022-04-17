import React from 'react';

function NavBar(props) {
    return (
        <nav className='navbar navbar-expand-lg Navbar'>
            <button className='nav-link'>{props.userName}</button>
        </nav>
    )
}

export default NavBar;