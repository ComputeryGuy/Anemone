import React, { useState, useContext } from "react";
import { useNavigate } from 'react-router-dom';

import * as Components from '../styles/Components';
import AuthContext from "../store/auth-context";

function AuthPage() {
    const navigate = useNavigate();
    const authCtx = useContext(AuthContext);

    const [inputEmail, setInputEmail] = useState('');
    const [inputPW, setInputPW] = useState('');
    const [inputName, setInputName] = useState('');

    const [isSignIn, setIsSingIn] = useState(true);
    const [isLoading, setIsLoading] = useState(false);

    const handleInputEmail = (e) => {
        setInputEmail(e.target.value);
    }

    const handleInputPW = (e) => {
        setInputPW(e.target.value);
    }

    const handleInputName = (e) => {
        setInputName(e.target.value);
    }

    function submitHandler(event) {
        event.preventDefault();

        setIsLoading(true);
        if (isSignIn) {
            fetch(
                'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyCyVpMe3Kgx5tfdgFd1iVNz3JMUKo8mHSA',
                {
                    method: 'POST',
                    body: JSON.stringify({
                        email: inputEmail,
                        password: inputPW,
                        returnSecureToken: true
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            ).then(res => {
                setIsLoading(false);
                if (res.ok) {
                    return res.json().then(data => {
                        authCtx.login(data.idToken);
                        navigate('/');
                    });
                } else {
                    return res.json().then(data => {
                        let errorMessage = 'Authentication failed!';
                        if (data && data.error && data.error.message) {
                            errorMessage = data.error.message;
                        }
                        alert(errorMessage);
                    });
                }
            });
        } else {

            fetch(
                'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyCyVpMe3Kgx5tfdgFd1iVNz3JMUKo8mHSA',
                {
                    method: 'POST',
                    body: JSON.stringify({
                        email: inputEmail,
                        password: inputPW,
                        returnSecureToken: true
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }
            ).then(res => {
                setIsLoading(false);
                if (res.ok) {
                    return res.json().then(() => {
                        alert('Success');
                        navigate('/');
                    });
                } else {
                    return res.json().then(data => {
                        let errorMessage = 'Authentication failed!';
                        if (data && data.error && data.error.message) {
                            errorMessage = data.error.message;
                        }
                        alert(errorMessage);
                    });
                }
            });
        }
    }

    return (
        <Components.Container>
            <Components.SignUpContainer signinIn={isSignIn}>
                <Components.Form onSubmit={submitHandler}>
                    <Components.Title>Create Account</Components.Title>
                    <Components.Input type='text' placeholder='Name' required value={inputName} onChange={handleInputName} />
                    <Components.Input type='email' placeholder='Email' required value={inputEmail} onChange={handleInputEmail} />
                    <Components.Input type='password' placeholder='Password' required value={inputPW} onChange={handleInputPW} />
                    {/* <Components.Input type='password' placeholder='Password Confirm' /> */}
                    {isLoading ?
                        <Components.Button>Loading...</Components.Button> :
                        <Components.Button>Sign Up</Components.Button>
                    }
                </Components.Form>
            </Components.SignUpContainer>

            <Components.SignInContainer signinIn={isSignIn}>
                <Components.LogoB>Anemone</Components.LogoB>
                <Components.Form onSubmit={submitHandler}>
                    <Components.Title>Sign in</Components.Title>
                    <Components.Input type='email' placeholder='Email' required value={inputEmail} onChange={handleInputEmail} />
                    <Components.Input type='password' placeholder='Password' required value={inputPW} onChange={handleInputPW} />
                    <Components.Anchor href='#'>Forgot your password?</Components.Anchor>
                    {isLoading ?
                        <Components.Button>Loading...</Components.Button> :
                        <Components.Button>Sign In</Components.Button>
                    }
                </Components.Form>
            </Components.SignInContainer>

            <Components.OverlayContainer signinIn={isSignIn}>
                <Components.Overlay signinIn={isSignIn}>

                    <Components.LeftOverlayPanel signinIn={isSignIn}>
                        <Components.LogoW>Anemone</Components.LogoW>
                        <Components.Title>Welcome Back!</Components.Title>
                        <Components.Paragraph>
                            To keep connected with us please login with your personal info
                        </Components.Paragraph>
                        <Components.GhostButton onClick={() => setIsSingIn(true)}>
                            Sign In
                        </Components.GhostButton>
                    </Components.LeftOverlayPanel>

                    <Components.RightOverlayPanel signinIn={isSignIn}>
                        <Components.Title>New to Anemone</Components.Title>
                        <Components.Title>Click below</Components.Title>
                        <Components.Paragraph>
                            {/* Enter Your personal details and start journey with us */}
                        </Components.Paragraph>
                        <Components.GhostButton onClick={() => setIsSingIn(false)}>
                            Sign Up
                        </Components.GhostButton>
                    </Components.RightOverlayPanel>

                </Components.Overlay>
            </Components.OverlayContainer>

        </Components.Container>
    )
}

export default AuthPage;