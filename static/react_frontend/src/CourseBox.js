import React, { Component } from 'react';
import Course from './Course';

class CourseBox extends Component {
    render(){
        return (
            <div class="card">
                <div class="card-header text-dark list-group-item-dark">Available Courses</div>
                <ul class="list-group">
                    <Course class="card-body"></Course>
                    <Course class="card-body w-100"></Course>
                </ul>
            </div>
        );

    }
}

export default CourseBox;