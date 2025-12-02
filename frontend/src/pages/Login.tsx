import React, { useState } from 'react';
import API from '../api';
export default function Login(){
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const submit = async (e:any)=>{
e.preventDefault();
const res = await API.post('/auth/login', { email, password });
localStorage.setItem('token', res.data.access_token);
alert('logged');
}
return (
   <form onSubmit={submit} style={{padding:20}}>
      <input placeholder='email' value={email} onChange={e=>setEmail(e.target.value)} />
      <input placeholder='password' type='password' value={password} onChange={e=>setPassword(e.target.value)} />
      <button>Login</button>
   </form>
   )
}