import firebase from 'firebase/app';
import 'firebase/auth';

const config = {
  apiKey: "AIzaSyDxEz4N4NAmbP0eokN1OQz66q-f5qPoFEY",
  authDomain: "avsummarizer.firebaseapp.com",
  databaseURL: "https://avsummarizer.firebaseio.com",
  projectId: "avsummarizer",
  storageBucket: "avsummarizer.appspot.com",
  messagingSenderId: "840471656370",
  appId: "1:840471656370:web:59e44c6520075562d4d6ab",
  measurementId: "G-R5N2XRJGQZ"
};

if (!firebase.apps.length) {
  firebase.initializeApp(config);
}

const auth = firebase.auth();
export default auth;
