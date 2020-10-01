import React from 'react';
import logo from './logo.svg';
import AvailableCourseList from './AvailableCourseList.js';
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <AvailableCourseList></AvailableCourseList>
      </header>
    </div>
  );
}

export default App;
