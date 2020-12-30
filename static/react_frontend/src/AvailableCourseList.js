import React from 'react'
import CourseBox from './CourseBox';
import ajax from 'ajax';

class AvailableCourseList extends React.Component {

    state = {
      courses: []
    }

    componentDidMount() {
      ajax.get('http://localhost:5000/curriculum')
        .then(res => {
          console.log(res)
        })
    }

    render() {
        return (
          <box>
          <CourseBox></CourseBox>
          </box>
        );
    }
} export default AvailableCourseList;