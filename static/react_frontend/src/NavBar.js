import React from 'react';

function NavBar(props) {
    return (
        <header style={headerStyle}>
            <h1>{props.userName}</h1>
        </header>
    )
}

const headerStyle = {
    textAlign: 'right',
    padding: '10px'
}

export default NavBar;