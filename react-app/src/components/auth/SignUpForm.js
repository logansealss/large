import React, { useState, useRef, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';

import { testInputStr, minStrLengthFunc, maxStrLengthFunc } from '../../utils/InputValidation';
import { signUp } from '../../store/session';

const SignUpForm = ({ onClose }) => {
  const mountedRef = useRef(true)

  const [username, setUsername] = useState('');
  const [usernameErr, setUsernameErr] = useState()
  const [email, setEmail] = useState('');
  const [emailErr, setEmailErr] = useState()
  const [password, setPassword] = useState('');
  const [passwordErr, setPasswordErr] = useState()
  const [firstName, setFirstName] = useState('');
  const [firstNameErr, setFirstNameErr] = useState()
  const [lastName, setLastName] = useState('');
  const [lastNameErr, setLastNameErr] = useState()
  const [repeatPassword, setRepeatPassword] = useState('');
  const [repeatPasswordErr, setRepeatPasswordErr] = useState()
  const [submitted, setSubmitted] = useState(false)
  const dispatch = useDispatch();
  const history = useHistory()

  const isNoLength = minStrLengthFunc(0)
  const isFortyChars = maxStrLengthFunc(41)
  const isFiftyChars = maxStrLengthFunc(51)
  const isTwoFiftyFiveChars = maxStrLengthFunc(256)
  const strMatch = (str1) => (str2) => (str1 !== str2)

  useEffect(() => {
    mountedRef.current = false
  }, [])



  useEffect(() => {
    if (submitted) {
      testInputStr(username,
        setUsernameErr,
        [isNoLength, isFortyChars],
        ['Username is required', 'Username must be 40 characters or less'])
    }
  }, [username])

  useEffect(() => {
    if (submitted) {
      testInputStr(email,
        setEmailErr,
        [isNoLength, isTwoFiftyFiveChars],
        ['Email is required', 'Email must be 255 characters or less'])
    }
  }, [email])

  useEffect(() => {
    if (submitted) {
      testInputStr(firstName,
        setFirstNameErr,
        [isNoLength, isFiftyChars],
        ['First name is required', 'First name must be 50 characters or less'])
    }
  }, [firstName])

  useEffect(() => {
    if (submitted) {
      testInputStr(lastName,
        setLastNameErr,
        [isNoLength, isFiftyChars],
        ['Last name is required', 'Last name must be 50 characters or less'])
    }
  }, [lastName])

  useEffect(() => {
    if (submitted) {
      testInputStr(password,
        setPasswordErr,
        [isNoLength],
        ['Password is required'])
    }
  }, [password])

  useEffect(() => {
    if (submitted) {
      testInputStr(repeatPassword,
        setRepeatPasswordErr,
        [isNoLength],
        ['Repeat password is required'])
    }
  }, [repeatPassword])

  useEffect(() => {
    if (submitted) {
      testInputStr(repeatPassword,
        setRepeatPasswordErr,
        [isNoLength, strMatch(password)],
        ['Repeat password is required', 'Repeat password must match password'])
    }
  }, [repeatPassword, password])

  const onSignUp = async (e) => {
    e.preventDefault();

    setSubmitted(true)

    const usernameTest = testInputStr(username,
      setUsernameErr,
      [isNoLength, isFortyChars],
      ['Username is required', 'Username must be 40 characters or less'])

    const emailTest = testInputStr(email,
      setEmailErr,
      [isNoLength, isTwoFiftyFiveChars],
      ['Email is required', 'Email must be 255 characters or less'])

    const firstNameTest = testInputStr(firstName,
      setFirstNameErr,
      [isNoLength, isFiftyChars],
      ['First name is required', 'First name must be 50 characters or less'])

    const lastNameTest = testInputStr(lastName,
      setLastNameErr,
      [isNoLength, isFiftyChars],
      ['Last name is required', 'Last name must be 50 characters or less'])

    const passwordTest = testInputStr(password,
      setPasswordErr,
      [isNoLength],
      ['Password is required'])

    const repeatPasswordTest = testInputStr(repeatPassword,
      setRepeatPasswordErr,
      [isNoLength, strMatch(password)],
      ['Repeat password is required', 'Repeat password must match password'])

    if (usernameTest && firstNameTest && lastNameTest && emailTest && passwordTest && repeatPasswordTest) {
      const data = await dispatch(signUp(username, email, firstName, lastName, password));
      if (data) {
        for(let err of data){
          let [type, error] = err.split(' : ')
          if(type === "username"){
            setUsernameErr(error)
          }else{
            setEmailErr(error)
          }
        }
      } else if (mountedRef.current) {
        onClose()
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value)
  }

  const updatelastName = (e) => {
    setLastName(e.target.value)
  }

  return (
    <form
      onSubmit={onSignUp}
      id='auth-form'
    >
      <div>
      </div>
      <div>
        <label
          htmlFor='username'
          className={submitted && usernameErr && 'validation-error'}
        >
          {submitted && usernameErr ? usernameErr : 'Username'}
        </label>
        <br></br>
        <input
          type='text'
          name='username'
          onChange={updateUsername}
          value={username}
          placeholder="Username"
        ></input>
      </div>
      <div>
        <label
          htmlFor='email'
          className={submitted && emailErr ? 'validation-error' : undefined}
        >
          {submitted && emailErr ? emailErr : 'Email'}
        </label>
        <br></br>
        <input
          type='email'
          name='email'
          onChange={updateEmail}
          value={email}
          placeholder="Email"
        ></input>
      </div>
      <div>
        <label
          htmlFor='firstName'
          className={submitted && firstNameErr ? 'validation-error' : undefined}
        >
          {submitted && firstNameErr ? firstNameErr : 'First name'}
        </label>
        <br></br>
        <input
          type='text'
          name='firstName'
          onChange={updateFirstName}
          value={firstName}
          placeholder="First name"
        ></input>
      </div>
      <div>
        <label
          htmlFor='lastName'
          className={submitted && lastNameErr ? 'validation-error' : undefined}
        >
          {submitted && lastNameErr ? lastNameErr : 'Last name'}
        </label>
        <br></br>
        <input
          type='text'
          name='lastName'
          onChange={updatelastName}
          value={lastName}
          placeholder="Last name"
        ></input>
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
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
          placeholder="Password"
        ></input>
      </div>
      <div>
        <label
          htmlFor='repeatPassword'
          className={submitted && repeatPasswordErr ? 'validation-error' : undefined}
        >
          {submitted && repeatPasswordErr ? repeatPasswordErr : 'Repeat password'}
        </label>
        <br></br>
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          placeholder="Repeat password"
        ></input>
      </div>
      <button
        type='submit'
        id="navbar-button"
        className="color-two auth-form-button"
      >Sign Up</button>
    </form>
  );
};

export default SignUpForm;
