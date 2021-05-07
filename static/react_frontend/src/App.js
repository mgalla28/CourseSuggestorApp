import React, { useState, useEffect } from 'react';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar.js';
import CourseBox from './components/CourseBox';

/*
Global state data needed:
user
backend api
*/

const backendServer = 'http://localhost:5000';
var dataLoaded = false;

function App() {

  const fetchAllCourses = async () => {
    
    const res = await fetch(backendServer + '/curriculum')
    const data = await res.json()
    setAvailableCourses(data['courses'])
    
  };

  const [user] = useState({userName: 'Guest'});
  const [availableCourses, setAvailableCourses] = useState([]);
  useEffect(() => {
    fetchAllCourses()
  }, [])


  console.log('else')
  return (
    <div className="App">
      <NavBar userName={user.userName} />
      <div className="App-body">
        <CourseBox title="Taken Courses" courseList={[]}/>
        <CourseBox title="Next Semester Schedule" courseList={[]}/>
        <CourseBox title="Available Courses" id="AvailableCourseList" courseList={availableCourses}/>        
      </div>
    </div>
  );
  

}

export default App;
