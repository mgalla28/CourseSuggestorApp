import React, { useState, useEffect } from 'react';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Login from './components/Login.js'
import NavBar from './components/NavBar.js';
import CourseBox from './components/CourseBox';
import SaveChangesButton from './components/SaveChangesButton';
import SuggestCoursesButton from './components/SuggestCoursesButton';

function App() {

  const fetchAllCourses = async () => {
    
    const res = await fetch('/curriculum')
    const data = await res.json()
    setAvailableCourses(data['courses'])
    
  };

  const [user, setUser] = useState();
  const [availableCourses, setAvailableCourses] = useState([]);
  const [nextSemesterCourses, setNextSemesterCourses] = useState([]);
  const [takenCourses, setTakenCourses] = useState([]);
  useEffect(() => {
    fetchAllCourses()
  }, [])

function availableCoursesClick (e) {
  const courseText = e.currentTarget.textContent;
  const courseName = courseText.slice(0, 6)
  setNextSemesterCourses(nextSemesterCourses.concat([{'course_identifier': courseName, 'credit_hours': 3}]))
  setAvailableCourses(availableCourses.filter(course => !(course.course_identifier === courseName)))
}

function nextSemesterCoursesClick (e) {
  const courseText = e.currentTarget.textContent;
  const courseName = courseText.slice(0, 6)
  setAvailableCourses(availableCourses.concat([{'course_identifier': courseName, 'credit_hours': 3}]))
  setNextSemesterCourses(nextSemesterCourses.filter(course => !(course.course_identifier === courseName)))
}

  if (!user) {
    const userData = window.localStorage.getItem('USER');
    if (userData != null)
        setUser(userData)
    else
        return <Login setUser={setUser} setTakenCourses={setTakenCourses} availableCourses={availableCourses} setAvailableCourses={setAvailableCourses}/>
  }

  return (
    <div className="App">
      <NavBar userName={user} />
      <div className="App-body">
        <SaveChangesButton nextSemesterCourses={nextSemesterCourses} setNextSemesterCourses={setNextSemesterCourses} setTakenCourses={setTakenCourses} user={user}/>
        <SuggestCoursesButton nextSemesterClasses={nextSemesterCourses} 
                              availableCourses={availableCourses}
                              setNextSemesterCourses={setNextSemesterCourses}
                              setAvailableCourses={setAvailableCourses}
                              takenCourses={takenCourses} />
        <div className="row">
          <CourseBox title="Taken Courses" courseList={takenCourses}/>
          <CourseBox title="Next Semester Schedule" courseList={nextSemesterCourses} courseClickFunction={nextSemesterCoursesClick}/>
          <CourseBox title="Available Courses" id="AvailableCourseList" courseList={availableCourses} courseClickFunction={availableCoursesClick}/>        
        </div>
      </div>
    </div>
  );
  

}

export default App;
