import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { connect } from 'react-redux';
import propTypes from 'prop-types';
import { login } from '../actions/auth';

const Login = ({ login, isAuthenticated }) => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const { username, password } = formData;

    const onChange = (e) =>
        setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = (e) => {
        e.preventDefault();

        login(username, password);
    };

    if (isAuthenticated) return <Redirect to="/" />;

    return (
        <div>
            <Helmet>
                <title>Login Page</title>{' '}
                <meta name="description" content="login page content"></meta>
            </Helmet>
            <h1>Sign in</h1>
            <p>Sign into your account</p>
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
                        type="password"
                        placeholder="Password"
                        name="password"
                        value={password}
                        onChange={(e) => onChange(e)}
                        minLength="6"
                    />
                </div>
                <button>Login</button>
            </form>
            <p>
                Dont have an account? <Link to="/signup">Sign Up</Link>
            </p>
        </div>
    );
};

Login.propTypes = {
    login: propTypes.func.isRequired,
    isAuthenticated: propTypes.bool,
};

const mapStateToProps = (state) => ({
    isAuthenticated: state.authReducer.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
