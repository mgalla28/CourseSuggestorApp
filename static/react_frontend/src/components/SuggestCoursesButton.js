import React from 'react';



const SuggestCoursesButton = ({nextSemesterClasses, availableCourses, setNextSemesterCourses, setAvailableCourses, takenCourses}) => {
    const suggestCourses = async () => {
        const courses = takenCourses.concat(nextSemesterClasses);

        const res = await fetch('/suggest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(courses)
        });

        if (res.ok) {
            const data = await res.json()
            setNextSemesterCourses(nextSemesterClasses.concat(data))
            setAvailableCourses(availableCourses.filter(course => {
                let retVal = true;
                data.forEach((element) => {                    
                    if (element.course_identifier === course.course_identifier) {
                        retVal = false;
                    }
                })
                return retVal;
            }))
        }
    }

    return (
        <button className="btn btn-secondary m-1" onClick={suggestCourses}>Suggest Next Semester Courses</button>
    )
}

export default SuggestCoursesButton;