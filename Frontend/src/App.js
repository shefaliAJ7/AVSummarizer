import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Route, Switch } from 'react-router-dom';
import { Layout, Icon } from 'antd';
import LoginContainer from './containers/LoginContainer';
import MainContainer from './containers/MainContainer';
import auth from './helpers/firebase';
import * as actions from './actions';
import './assets/css/App.css';


const { Header, Footer, Content } = Layout;
const loadingIcon = <Icon type="loading" style={{ fontSize: 34 }} spin />;

class App extends Component {
  constructor(props) {
    super(props);
    auth.onAuthStateChanged(props.actions.loginStateChange);
  }

  componentWillReceiveProps(nextProps) {
    if (this.props.store.user.empty === true
      || nextProps.store.user.isAuthenticated !== this.props.store.user.isAuthenticated) {
      this.props.history.push(`${global.BASE_PATH}/${auth.currentUser !== null ? 'main' : 'login'}`);
    }
  }

  render() {
    return (
      <Layout >
           <Switch>
             <Route exact path={`${global.BASE_PATH}/login`} component={LoginContainer} />
             <Route exact path={`${global.BASE_PATH}/main`} render={()=> <MainContainer auth={auth}/>} />
           </Switch>
       </Layout>

    );
  }
}

App.propTypes = {
  history: PropTypes.shape({
    push: PropTypes.func.isRequired,
  }).isRequired,
  actions: PropTypes.shape({
    logout: PropTypes.func.isRequired,
    loginStateChange: PropTypes.func.isRequired,
  }).isRequired,
  store: PropTypes.shape({
    data: PropTypes.object.isRequired,
    user: PropTypes.object.isRequired,
  }).isRequired,
};

const mapStateToProps = state => ({
  store: state,
});

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(actions, dispatch),
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
