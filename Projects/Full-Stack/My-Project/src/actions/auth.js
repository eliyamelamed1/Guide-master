import axios from 'axios';
import { setAlertMsgAndType } from './alert';
import {
  SIGNUP_SUCCESS,
  SIGNUP_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
} from './types';

export const login = (email, password) => async (dispatch) => {
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const body = JSON.stringify({ email, password });

  try {
    const res = await axios.post(
      `${process.env.REACT_APP_API_URL}/api/token/`,
      body,
      config
    );

    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data,
    });

    dispatch(setAlertMsgAndType('Authenticated successfully', 'success'));
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL,
    });
    dispatch(setAlertMsgAndType('Error Authenticating', 'error'));
  }
};

export const signUp = ({ name, email, password, password2 }) => async (
  dispatch
) => {
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const body = JSON.stringify({ name, email, password, password2 });

  try {
    const res = await axios.post(
      `${process.env.REACT_APP_API_URL}/accounts/signup/`,
      body,
      config
    );

    dispatch({
      type: SIGNUP_SUCCESS,
      payload: res.data,
    });

    dispatch(login(email, password));
  } catch (err) {
    dispatch({
      type: SIGNUP_FAIL,
    });
    dispatch(setAlertMsgAndType('Error Authenticating', 'error'));
  }
};
export const logout = () => (dispatch) => {
  dispatch(setAlertMsgAndType('logout successful.', 'success'));
  dispatch({ type: LOGOUT });
};
