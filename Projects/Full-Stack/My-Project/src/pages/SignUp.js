import React, { useState } from 'react';
import { connect } from 'react-redux';
import { Link, Redirect } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { setAlertMsgAndType } from '../actions/alert';
import { signup } from '../actions/auth';
import PropTypes from 'prop-types';

const SignUp = ({ setAlertMsgAndType, signup, isAuthenticated }) => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirm_password: '',
    });

    const { username, email, password, confirm_password } = formData;

    const onChange = (e) =>
        setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = (e) => {
        e.preventDefault();

        if (password !== confirm_password)
            setAlertMsgAndType('Passwords do not match', 'error');
        else signup({ username, email, password, confirm_password });
    };

    if (isAuthenticated) return <Redirect to="/" />;

    return (
        <div>
            <Helmet>
                <title>Create New account</title>
                <meta name="description" content="sign up page" />
            </Helmet>
            <h1>Sign Up</h1>
            <p>Create your account</p>
            <form onSubmit={(e) => onSubmit(e)}>
                <div>
                    <input
                        type="text"
                        placeholder="Username"
                        name="username"
                        value={username}
                        onChange={(e) => onChange(e)}
                        required
                    />
                    <input
                        type="email"
                        placeholder="Email"
                        name="email"
                        value={email}
                        onChange={(e) => onChange(e)}
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        name="password"
                        value={password}
                        onChange={(e) => onChange(e)}
                        minLength="6"
                    />
                    <input
                        type="password"
                        placeholder="Confirm password"
                        name="confirm_password"
                        value={confirm_password}
                        onChange={(e) => onChange(e)}
                        minLength="6"
                    />
                </div>
                <button>Register</button>
            </form>
            <p>
                Already have an account? <Link to="/login">Sign in</Link>
            </p>
        </div>
    );
};

SignUp.propTypes = {
    setAlertMsgAndType: PropTypes.func.isRequired,
    signup: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool,
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.authReducer.isAuthenticated,
});

export default connect(mapStateToProps, { setAlertMsgAndType, signup })(SignUp);
