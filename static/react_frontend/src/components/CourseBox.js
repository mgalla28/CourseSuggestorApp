import React from 'react';
import Course from './Course';

const CourseBox = ({ title, courseList }) => {
    return (
        <div className="card float-left" style={{ paddingLeft: 125, paddingRight: 125, backgroundColor: '#282c34'}}>
            <div className="card-header text-dark list-group-item-dark">{title}</div>
            <ul className="list-group" style={{maxHeight: '500px', overflowY: 'scroll'}}>
                {courseList.map((course) => <Course courseName={course.course_identifier} creditHours={course.credit_hours}/>)}
            </ul>
        </div>
    );
}

export default CourseBox