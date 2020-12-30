import React, { useState } from 'react';
import logo from './logo.svg';
import AvailableCourseList from './AvailableCourseList.js';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import NavBar from './NavBar.js';

/*
Global state data needed:
user
backend api


*/


function App() {
  
  const [user, setUser] = useState({userName: 'Guest'});

  return (
    <div className="App">
      <NavBar userName={user.userName} />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <AvailableCourseList></AvailableCourseList>
      </header>
    </div>
  );
}

export default App;
