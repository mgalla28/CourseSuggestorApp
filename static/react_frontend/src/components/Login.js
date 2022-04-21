import React, { useState } from 'react';



function Login({setUser, setTakenCourses, availableCourses, setAvailableCourses}) {
    const [userName, setUserName] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault()        
        document.body.style.cursor='wait'
        const loginInfo = {userName, password}
        const res = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginInfo)
        });

        if (res.ok) {
            const data = await res.json()
            if ('username' in data){
                setUser(data['username'])
                setTakenCourses(data['courses_completed'])
                // Remove taken courses from available courses
                setAvailableCourses(availableCourses.filter(course => {
                    let retVal = true;
                    data['courses_completed'].forEach((element) => {                    
                        if (element.course_identifier === course.course_identifier) {
                            retVal = false;
                        }
                    })
                    return retVal;
                }))
                document.body.style.cursor='initial'
            }
        }
        else {
            alert('Bad login');
            document.body.style.cursor='initial';
        }
    }

    const loginAsGuest = async (e) =>
    {
        e.preventDefault();
        document.body.style.cursor='wait';
        const res = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({userName: 'Guest', password:''})
        });

        if (res.ok) {
            const data = await res.json()
            if ('username' in data){
                setUser(data['username'])
                document.body.style.cursor='initial'
            }
        }
        else {
            alert('Login as guest failed');
            document.body.style.cursor='initial';
        }
    }

    return(
        <div className='Login-body'>
            <div className="card text-white border border-dark Login-card">
                <h1 className='card-title text-center' style={{marginTop: 20}}>Course Suggestor</h1>
                <div className='card-body'>
                    <form onSubmit={handleSubmit}> 
                        <div className="d-flex flex-column">
                            <label>Username</label>
                            <input onChange={(e) => setUserName(e.target.value)}></input>
                            <label>Password</label>
                            <input type="password" onChange={(e) => setPassword(e.target.value)}></input>
                            <button className="btn btn-secondary mt-3" type='submit'>Login</button>
                            <button className="btn btn-secondary mt-2" onClick={loginAsGuest}>Login as Guest</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login;