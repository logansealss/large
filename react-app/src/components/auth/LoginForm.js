import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';

import { testInputStr, minStrLengthFunc } from '../../utils/InputValidation';
import { login } from '../../store/session';

const LoginForm = ({ onClose }) => {
  const [email, setEmail] = useState('');
  const [emailErr, setEmailErr] = useState()
  const [passwordErr, setPasswordErr] = useState()
  const [password, setPassword] = useState('');
  const [submitted, setSubmitted] = useState(false)
  const dispatch = useDispatch();
  const history = useHistory()

  async function demoUserLogin(e) {
    e.preventDefault()
    const data = await dispatch(login('davidrogers@user.io', 'password'));
  }

  const isNoLength = minStrLengthFunc(0)

  const onLogin = async (e) => {
    e.preventDefault();

    setSubmitted(true)

    const validEmail = testInputStr(email, setEmailErr, [isNoLength], ['Email is required'])
    const validPassword = testInputStr(password, setPasswordErr, [isNoLength], ['Password is required'])

    if (!validEmail || !validPassword) {
      return
    }

    const data = await dispatch(login(email, password));
    if (data) {
      const [head, tail] = data[0].split(' : ')
      console.log('head and tail', head, tail)
      if (head === 'email') {
        setEmailErr(tail);
      } else {
        setPasswordErr(tail)
      }
    } else {
      setEmailErr()
      setPasswordErr()
    }
  };

  useEffect(() => {
    if (submitted) {
      testInputStr(password, setPasswordErr, [isNoLength], ['Password is required'])
    }
  }, [password])


  useEffect(() => {
    if (submitted) {

      testInputStr(email, setEmailErr, [isNoLength], ['Email is required'])
    }
  }, [email])

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  return (
    <form
      onSubmit={onLogin}
      id='auth-form'
    >
      <div>
        <label
          htmlFor='email'
          className={submitted && emailErr ? 'validation-error' : undefined}
        >
          {submitted && emailErr ? emailErr : 'Email'}
        </label>
        <br></br>
        <input
          name='email'
          type='email'
          placeholder='Email'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div>
        <label
          htmlFor='password'
          className={submitted && passwordErr ? 'validation-error' : undefined}
        >
          {submitted && passwordErr ? passwordErr : 'Password'}
        </label>
        <br></br>
        <input
          name='password'
          type='password'
          placeholder='Password'
          value={password}
          onChange={updatePassword}
        />
      </div>
      <button
        type='submit'
        id="navbar-button"
        className="color-two auth-form-button"
      >Login</button>
      <button
        type='submit'
        id="navbar-button"
        className="color-two auth-form-button"
        onClick={demoUserLogin}
      >Demo User Login</button>
    </form>
  );
};

export default LoginForm;
