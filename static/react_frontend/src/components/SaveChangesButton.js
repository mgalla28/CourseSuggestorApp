import React from 'react';

function saveChanges () {
    console.log('Post data to user account')
}

const SaveChangesButton = () => {
    return (
        <button className="btn btn-primary" onClick={saveChanges}>Save Changes</button>
    )
}

export default SaveChangesButton;