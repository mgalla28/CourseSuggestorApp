import React, { useState, useEffect } from 'react';



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
        setUser({res})
        document.body.style.cursor='initial'
    }

    return(
        <form onSubmit={handleSubmit}> 
            <label>Username</label>
            <input value={userName} onChange={(e) => setUserName(e.target.value)}></input>
            <label>Password</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)}></input>
            <button type='submit'>Login</button>
            <button>Login as Guest</button>
        </form>
    )
}

export default Login;