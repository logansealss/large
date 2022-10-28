import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import Navbar from './components/Navbar/Navbar'
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import LandingPage from './components/LandingPage/LandingPage';
import PostForm from './components/PostFormPage/PostForm/PostForm';
import { authenticate } from './store/session';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Navbar></Navbar>
      <Switch>
        <Route exact path='/'>
          <LandingPage></LandingPage>
        </Route>
        <Route exact path='/new-post'>
          <PostForm></PostForm>
        </Route>
        <Route exact path='/signup'>
          <SignUpForm></SignUpForm>
        </Route>
        <Route exact path='/login'>
          <LoginForm></LoginForm>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
