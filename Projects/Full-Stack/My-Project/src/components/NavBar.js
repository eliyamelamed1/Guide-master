import React, { Fragment } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';
import Alert from './Alert';
import PropTypes from 'prop-types';

const NavBar = ({ authReducer: { isAuthenticated, loading }, logout }) => {
    const authLinks = (
        <a onClick={logout} href="#">
            Logout
        </a>
    );

    const guestLinks = (
        <Fragment>
            <Link to="/login">Login</Link>
            <Link to="/signup">Sign up</Link>
        </Fragment>
    );
    return (
        <Fragment>
            <nav>
                <div>
                    <div>
                        <Link to="/">Recipe site</Link>
                    </div>
                    <div>
                        {!loading && (
                            <Fragment>
                                {isAuthenticated ? authLinks : guestLinks}
                            </Fragment>
                        )}
                    </div>
                </div>
                <div>
                    <li>
                        <NavLink exact to="/">
                            Home
                        </NavLink>
                    </li>
                    <li>
                        <NavLink exact to="/recipe">
                            recipe
                        </NavLink>
                    </li>
                    <li>
                        <NavLink exact to="/about">
                            about
                        </NavLink>
                    </li>
                    <li>
                        <NavLink exact to="/contact">
                            contact
                        </NavLink>
                    </li>
                </div>
            </nav>
            <Alert />
        </Fragment>
    );
};

NavBar.propTypes = {
    logout: PropTypes.func.isRequired,
    authReducer: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
    authReducer: state.authReducer,
});

export default connect(mapStateToProps, { logout })(NavBar);
