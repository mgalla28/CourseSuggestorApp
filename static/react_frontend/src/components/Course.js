import React from 'react';

const Course = ({ courseName, creditHours, key, click }) => {
    return (
        <li className="list-group-item Course" style={{ margin: '0px', cursor: 'pointer' }} draggable="true" onClick={click} key={key}>
            <div style={{ float: 'left', border: 'solid', padding: '20px', margin: '0px'}}>{ courseName }</div>
            <div style={{ float: 'right', border:'solid', padding: '20px', margin: '0px' }}>{ creditHours }</div>
        </li> 
        );
}

export default Course;