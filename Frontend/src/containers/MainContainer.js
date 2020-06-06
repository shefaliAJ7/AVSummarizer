import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Row, Layout, Col, Card,  Menu, Breadcrumb, Carousel, Button } from 'antd';

import * as actions from '../actions';

import range from 'lodash/range';
import comp from '../assets/img/computer.jpg';

import $ from 'jquery';

import 'react-toastify/dist/ReactToastify.css';

import DetailsForm from '../components/Form.js';







class MainContainer extends React.Component {
  constructor(props) {
    super(props);
    document.title = 'AvSummarizer | App';

    this.state = {allData : null};
  };

  filterList(){
    console.log("Search")
  }

  render() {
    var that = this;


    return (
    <React.Fragment>
      <div
          style={{
            width: '100%',
            height:"6vh",
            backgroundColor:"#000000"
          }}
        >
          {
            this.props.auth.currentUser !== null && (
              <div style={{ float: 'right',marginRight:'50px', marginTop:'1%'}}>
                <Button type="danger" icon="logout" shape="circle" size="small" onClick={this.props.actions.logout} />
              </div>
            )
          }
      </div>
      <div style={{ height:'100%' }}>
        <div style={{'textAlign': 'center'}}>
          <Col>
            <DetailsForm />
          </Col>
        </div>
      </div>
    </React.Fragment>
    );
  }
}

MainContainer.propTypes = {
  store: PropTypes.shape({
    ui: PropTypes.object.isRequired,
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

export default connect(mapStateToProps, mapDispatchToProps)(MainContainer);
