import React from 'react';

function saveChanges () {
    console.log('Post data to user account')
}

const SaveChangesButton = () => {
    return (
        <button className="btn btn-primary m-1" onClick={saveChanges}>Save Changes</button>
    )
}

export default SaveChangesButton;