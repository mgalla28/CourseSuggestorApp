import React, { useState } from 'react';



function Login({setUser, backendServer}) {
    const [userName, setUserName] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = async (e) =>{
        e.preventDefault()
        document.body.style.cursor='wait'
        const res = await fetch(backendServer + '/login', {
            method: 'POST',
            body: JSON.stringify(userName, password)
        }, () => document.body.style.cursor='initial')
        const data = await res.json()
        setUser(data['username'])
        document.body.style.cursor='initial'
    }

    return(
        <div className='Login-body'>
            <div className="card bg-dark text-white border border-dark">
                <h5 className='card-title text-center'>Course Suggestor</h5>
                <div className='card-body'>
                    <form onSubmit={handleSubmit}> 
                        <div class="d-flex flex-column">
                            <label>Username</label>
                            <input value={userName} onChange={(e) => setUserName(e.target.value)}></input>
                            <label>Password</label>
                            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
                            <button class="m-2" type='submit'>Login</button>
                            <button class="m-2">Login as Guest</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login;