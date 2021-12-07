import React, { useState, useEffect } from 'react';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar.js';
import CourseBox from './components/CourseBox';
import SaveChangesButton from './components/SaveChangesButton'

/*
Global state data needed:
user
backend api
*/

const backendServer = 'http://localhost:5000';

function App() {

  const fetchAllCourses = async () => {
    
    const res = await fetch(backendServer + '/curriculum')
    const data = await res.json()
    setAvailableCourses(data['courses'])
    
  };

  const [user] = useState({userName: 'Guest'});
  const [availableCourses, setAvailableCourses] = useState([]);
  const [nextSemesterClasses, setNextSemesterCourses] = useState([])
  useEffect(() => {
    fetchAllCourses()
  }, [])

function availableCoursesClick (e) {
  const courseText = e.currentTarget.textContent;
  const courseName = courseText.slice(0, 6)
  setNextSemesterCourses(nextSemesterClasses.concat([{'course_identifier': courseName, 'credit_hours': 3}]))
}


  return (
    <div className="App">
      <NavBar userName={user.userName} />
      <div className="App-body">
        <SaveChangesButton />
        <div>
          <CourseBox title="Taken Courses" courseList={[]}/>
          <CourseBox title="Next Semester Schedule" courseList={nextSemesterClasses}/>
          <CourseBox title="Available Courses" id="AvailableCourseList" courseList={availableCourses} courseClickFunction={availableCoursesClick}/>        
        </div>
      </div>
    </div>
  );
  

}

export default App;
