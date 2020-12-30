import React, { Component } from 'react';

class Course extends Component {
    render(){
        return (
        <li class="list-group-item list-group-item-primary" draggable="true">
            <table> {/*TODO: Is table the best way to do this?*/}
                <tr>
                    <td class="w-100">Course</td>
                    |  
                    <td>  3</td>
                </tr>
            </table>
        </li>
        );

    }
}

export default Course;