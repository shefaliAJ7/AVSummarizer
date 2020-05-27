import * as types from '../constants/actionTypes';

const initialState = {
  login_requested: false,
  logout_requested: false,
  login_failed: false,
  logout_failed: false,
};

const ui = (state = initialState, action) => {
  switch(action.type) {
    case types.USER_LOGIN_REQUESTED:
      return Object.assign({}, state, { login_requested: true, logout_requested: false });
    case types.USER_LOGOUT_REQUESTED:
      return Object.assign({}, state, { logout_requested: true, login_requested: false });
    default:
      return state;
  }
};

export default ui;
