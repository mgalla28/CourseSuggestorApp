import React from 'react';

const SaveChangesButton = ({nextSemesterCourses, setNextSemesterCourses, setTakenCourses, user}) => {

    const saveChanges = async () => {

        const course_identifiers = nextSemesterCourses.map(c => c['course_identifier'])
        const nextSemesterInfo = {user_name: user, courses: course_identifiers};
        console.log(nextSemesterInfo)
        const res = await fetch('/complete_courses', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nextSemesterInfo)
        });

        if (res.ok) {
            const data = await res.json()
            setTakenCourses(data)
            setNextSemesterCourses(nextSemesterCourses.filter(course => {
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
        <button className="btn btn-secondary m-1" onClick={saveChanges}>Save Changes</button>
    )
}

export default SaveChangesButton;