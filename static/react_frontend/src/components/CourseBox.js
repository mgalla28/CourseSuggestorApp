import React from 'react';
import Course from './Course';

const CourseBox = ({ title, courseList, courseClickFunction }) => {
    return (
        <div className="card float-left" style={{ paddingLeft: 90, paddingRight: 90, backgroundColor: '#282c34'}}>
            <div className="card-header text-dark list-group-item-dark">{title}</div>
            <ul className="list-group" style={{maxHeight: '500px', overflowY: 'scroll'}}>
                {courseList.map((course) => <Course courseName={course.course_identifier} creditHours={course.credit_hours} click={courseClickFunction}/>)}
            </ul>
        </div>
    );
}

export default CourseBox