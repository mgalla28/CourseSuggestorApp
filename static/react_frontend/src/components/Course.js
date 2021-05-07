import React from 'react';

const Course = ({ courseName, creditHours, key }) => {
    return (
        <li className="list-group-item list-group-item-primary" style={{ margin: '0px' }} draggable="true" key={key}>
            <div style={{ float: 'left', border: 'solid', padding: '20px', margin: '0px'}}>{ courseName }</div>
            <div style={{ float: 'right', border:'solid', padding: '20px', margin: '0px' }}>{ creditHours }</div>
        </li> 
        );
}

export default Course;