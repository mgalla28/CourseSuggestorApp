import React from 'react';

const Course = ({ courseName, creditHours }) => {
    return (
        <li className="list-group-item list-group-item-primary" draggable="true">
            <table>
                <tbody>
                    <tr>
                        <td className="w-100">{ courseName }</td>
                        <td>|</td>  
                        <td>{ creditHours }</td>
                    </tr>
                </tbody>
            </table>
        </li>
        );
}

export default Course;