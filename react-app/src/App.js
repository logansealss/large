import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import Navbar from './components/Navbar/Navbar'
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import LandingPage from './components/LandingPage/LandingPage';
import PostForm from './components/PostForm/PostForm';
import PostPage from './components/PostPage/PostPage';
import { authenticate } from './store/session';
import UpdatePostWrapper from './components/PostForm/UpdatePostWrapper';
import { AboutUserPage } from './components/AboutUserPage/AboutUserPage';

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
        <Route exact path='/posts/:postId'>
          <PostPage></PostPage>
        </Route>
        <Route exact path='/posts/:postId/edit'>
          <UpdatePostWrapper></UpdatePostWrapper>
        </Route>
        <Route path='/about'>
          <AboutUserPage></AboutUserPage>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
