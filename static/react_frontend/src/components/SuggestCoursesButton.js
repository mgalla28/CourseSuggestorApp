import React from 'react';

function suggestCourses () {
    console.log('Courses suggested')
}

const SuggestCoursesButton = () => {
    return (
        <button className="btn btn-primary m-1" onClick={suggestCourses}>Suggest Next Semester Courses</button>
    )
}

export default SuggestCoursesButton;