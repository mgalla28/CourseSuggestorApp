import React, { Component } from 'react';
import Course from './Course';

class CourseBox extends Component {
    render(){
        return (
            <div class="card">
                <div class="card-header text-dark">Available Courses</div>
                <ul class="list-group list-group-flush">
                    <Course class="card-body"></Course>
                </ul>
            </div>
        );

    }
}

export default CourseBox;