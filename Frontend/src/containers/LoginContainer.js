import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Row, Layout } from 'antd';
import LoginForm from '../components/LoginForm';
import * as actions from '../actions';

import firebase from "firebase";
import StyledFirebaseAuth from "react-firebaseui/StyledFirebaseAuth"
import auth from '../helpers/firebase';
import LandingPage from '.././components/LandingPage'
const { Content } = Layout;

if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: "AIzaSyDxEz4N4NAmbP0eokN1OQz66q-f5qPoFEY",
    authDomain: "avsummarizer.firebaseapp.com",
    databaseURL: "https://avsummarizer.firebaseio.com",
   projectId: "avsummarizer",
   storageBucket: "avsummarizer.appspot.com",
   messagingSenderId: "840471656370",
   appId: "1:840471656370:web:59e44c6520075562d4d6ab",
   measurementId: "G-R5N2XRJGQZ"
  })

}



class LoginContainer extends Component {
  uiConfig = {
     signInFlow: "popup",
     signInOptions: [
       firebase.auth.GoogleAuthProvider.PROVIDER_ID,
     ],
     callbacks: {
        signInSuccess: () => false
      }
  }
  constructor(props) {
    super(props);
  }
  componentDidMount() {
    document.title = 'AV_Summarizer | Login';
  }


  render() {
    return (
      <LandingPage uiConfig={this.uiConfig} firebaseAuth={firebase.auth()}/>
    );
  }
}

const mapStateToProps = state => ({
  store: state,
});

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(actions, dispatch),
});

export default connect(mapStateToProps, mapDispatchToProps)(LoginContainer);
