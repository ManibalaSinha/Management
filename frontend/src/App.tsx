import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Leads from './pages/Leads';
import Login from './pages/Login';

export default function App(){
   return (
      <BrowserRouter>
         <nav style={{padding:12}}>
            <Link to='/'>Leads</Link> | <Link to='/login'>Login</Link>
         </nav>
         <Routes>
            <Route path='/' element={<Leads/>} />
            <Route path='/login' element={<Login/>} />
         </Routes>
      </BrowserRouter>
   )
}