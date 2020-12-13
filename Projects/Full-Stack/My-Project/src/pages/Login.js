import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { Helmet } from 'react-helmet';
import { connect } from 'react-redux';
import propTypes from 'prop-types';
import { login } from '../actions/auth';

const Login = ({ login, isAuthenticated }) => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const { email, password } = formData;

    const onChange = (e) =>
        setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = (e) => {
        e.preventDefault();

        login(email, password);
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
    isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
