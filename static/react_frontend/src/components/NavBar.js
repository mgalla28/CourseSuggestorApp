import React from 'react';

function NavBar(props) {
    return (
        <nav className='navbar navbar-expand-lg navbar-light bg-dark'>
            <a className='nav-link' href='#'>{props.userName}</a>
        </nav>
    )
}

export default NavBar;