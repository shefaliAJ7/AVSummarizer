import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk';
import { createStore, compose, applyMiddleware } from 'redux';
import { Route, BrowserRouter as Router } from 'react-router-dom';
import rootReducer from './reducers';
import './assets/css/index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

const store = createStore(
  rootReducer,
  compose(
    applyMiddleware(thunk),
    global.devToolsExtension ? global.devToolsExtension() : f => f,
  )
);

global.BASE_PATH = window.location.hostname === 'localhost' ? '' : '';


// This code snippet is taken from semantic-react website for loading CSS for their components

// start
const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href = "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.head.appendChild(styleLink);
// end

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <Route path={global.BASE_PATH} component={App} />
    </Router>
  </Provider>,
  document.getElementById('root')
);

serviceWorker.unregister();
