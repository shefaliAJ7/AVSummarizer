import * as types from '../constants/actionTypes';

const user = (state = { empty: true }, action) => {
  switch (action.type) {
    case types.USER_LOGIN_SUCCESS:
      return { isAuthenticated: true };
    case types.USER_LOGOUT_SUCCESS:
      return { isAuthenticated: false };
    default:
      return state;
  }
};

export default user;
