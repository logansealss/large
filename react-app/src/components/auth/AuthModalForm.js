import { useState } from 'react'

import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";
import "../Navbar/AuthModal.css"


export default function AuthModalForm({ formToDisplay }) {

    const [isLoginForm, setIsLoginForm] = useState(formToDisplay)

    const toggleForm = () => {
        setIsLoginForm(val => !val)
    }

    return (
        <div>

            <div id="auth-form-container">
                <div id="auth-form-flex-padding">

                    <div
                        id="auth-form-header"
                    >
                        {isLoginForm ? 'Welcome back.' : 'Join Large.'}
                    </div>
                    {isLoginForm ? (
                        <>
                            <LoginForm></LoginForm>
                            <div
                                className='auth-form-toggle-container'
                            >
                                No account?
                                <span
                                    onClick={toggleForm}
                                    id='auth-form-toggle'
                                >
                                    {' Create one'}
                                </span>
                            </div>
                        </>
                    ) : (
                        <>
                            <SignUpForm></SignUpForm>
                            <div
                                className='auth-form-toggle-container'
                            >
                                Already have an account?
                                <span
                                    onClick={toggleForm}
                                    id='auth-form-toggle'
                                >
                                    {' Sign in'}
                                </span>
                            </div>
                        </>
                    )
                    }
                </div>
            </div>
        </div>
    )
}