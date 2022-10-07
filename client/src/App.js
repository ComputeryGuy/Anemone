import React, { useContext } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import MainPage from './pages/MainPage';
import AuthPage from './pages/AuthPage';
import AuthContext from './store/auth-context';

function App() {
  const authCtx = useContext(AuthContext);

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' 
          element={
            authCtx.isLoggedIn ?
            <MainPage /> :
            <Navigate to='/auth' />
          }
        ></Route>
        <Route path='/auth' 
          element={
            !authCtx.isLoggedIn ?
            <AuthPage /> :
            <Navigate to='/' />
          }
        ></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
