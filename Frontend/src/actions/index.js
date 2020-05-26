// import axios from 'axios';
import { message } from 'antd';
import auth from '../helpers/firebase';
import * as types from '../constants/actionTypes';

export function login(username, pass) {
  return (dispatch) => {
    dispatch({ type: types.USER_LOGIN_REQUESTED });
    var provider = new auth.GoogleAuthProvider();

    auth().signInWithPopup(provider).then(function(result) {
  // This gives you a Google Access Token. You can use it to access the Google API.
    var token = result.credential.accessToken;
    // The signed-in user info.
    var user = result.user;
    // ...
  }).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
    // The email of the user's account used.
    var email = error.email;
    // The firebase.auth.AuthCredential type that was used.
    var credential = error.credential;
    dispatch({ type: types.USER_LOGIN_FAILED, error: errorMessage });
    // ...
  });

  };
}

export function loginStateChange(user) {
  return (dispatch, getState) => {
    const state = getState();
    if (user && state.ui.login_requested) {
      message.success('Successfully logged in. Redirecting...', 2);
      setTimeout(() => { dispatch({ type: types.USER_LOGIN_SUCCESS }); }, 2000);
    } else if (user) {
      dispatch({ type: types.USER_LOGIN_SUCCESS });
    } else if (state.ui.logout_requested) {
      message.success('Successfully logged out. Redirecting...', 2);
      setTimeout(() => { dispatch({ type: types.USER_LOGOUT_SUCCESS }); }, 2000);
    } else {
      dispatch({ type: types.USER_LOGOUT_SUCCESS });
    }
  };
}

export function logout() {
  return (dispatch) => {
    dispatch({ type: types.USER_LOGOUT_REQUESTED });
    auth.signOut().catch((err) => {
      message.error('Logout failed!');
      dispatch({ type: types.USER_LOGOUT_FAILED, error: err });
    });
  };
}
