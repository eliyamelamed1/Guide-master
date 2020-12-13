import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import mergeReducers from './reducers/index';

const initialState = {};

const middleware = [thunk];

const store = createStore(
  mergeReducers,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware)) // add dev tools functionality
);

export default store;
