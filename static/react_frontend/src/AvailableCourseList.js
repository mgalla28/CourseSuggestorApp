import React from 'react'
import CourseBox from './CourseBox';

class AvailableCourseList extends React.Component {

    state = {
      courses: []
    }

    componentDidMount() {
      window.fetch('http://localhost:5000/curriculum',)
        .then(function (res) {
          res.json().then(function (data) {
            window.courses = data;
          })

        })
    }

    render() {
        return (
          <CourseBox></CourseBox>
        );
    }
} export default AvailableCourseList;