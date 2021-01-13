import React, { Component } from 'react';

class Course extends Component {
    render(){
        return (
        <li class="list-group-item list-group-item-primary" draggable="true">
            <table>
                <tbody>
                    <tr>
                        <td class="w-100">Course</td>
                        <td>|</td>  
                        <td>  3</td>
                    </tr>
                </tbody>
            </table>
        </li>
        );

    }
}

export default Course;