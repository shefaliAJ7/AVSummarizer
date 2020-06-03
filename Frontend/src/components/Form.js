import React, {Component} from 'react'
import { Button, Checkbox, Form, Header, Icon , Input, Loader, Dimmer} from 'semantic-ui-react'
import Tabs from '../components/Tabs.js';
import back from './../assets/img/back.png';

import { Row, Layout, Col, Card,  Menu, Breadcrumb, Carousel} from 'antd';
import _concat from "lodash/concat"
import _uniq from "lodash/uniq"
import _merge from "lodash/merge"
import _isEmpty from "lodash/isEmpty"
import { Left } from 'react-bootstrap/lib/Media';
import axios from 'axios';


const url_final = "http://127.0.0.1:5000/api/summarize";

const loadingIcon = <Loader />;

class DetailsForm extends React.Component {

  constructor(props) {
      super(props);
      this.state = {
        data:'',
        sysData:'',
        loading:false,
        min:'30',
        max:'100'
      };

      this.handleSearchChange = this.handleSearchChange.bind(this);
      this.handleMinChange = this.handleMinChange.bind(this);
      this.handleMaxChange = this.handleMaxChange.bind(this);
      this.fetchData = this.fetchData.bind(this);
  }


  handleSearchChange(event){

    this.setState({data: event.target.value});
  }
  handleMinChange(event){

    this.setState({min: event.target.value});
  }
  handleMaxChange(event){

    this.setState({max: event.target.value});
  }

  fetchData(){
    this.setState({loading:true});


    var d = {
	     "avlink": this.state.data,
       "min": this.state.min,
       "max":this.state.max,
    };

    fetch(url_final,{
      method: 'POST',
      mode: 'cors',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE',
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
			},
      body: JSON.stringify(d)
		}).then((response) => {
      this.setState({loading:false});
			if(response.status == 200){
        console.log("done", response);
				return response.json()
      }
			else {
				alert('Uh Oh! something went wrong!');
				return -1;
			}
    }).then((data) => {
			if(data == -1)
				return;
        console.log("Incoming data", data);
			this.setState({
				sysData:data
			});
		}
		)

  }


  render(){
    var loading = this.state.loading;
    return(
      <Row  style={{backgroundImage:"url(" + back + ")", padding:'15%', backgroundPosition: 'center',backgroundSize: 'cover',backgroundRepeat: 'no-repeat'}}>
        <Form >

          <Row style={{'fontSize':'20px'}}><Input style={{'width':'480px', 'height':'50px'}} value={this.state.data} placeholder='Enter Youtube Url...' onChange={this.handleSearchChange.bind(this)} /></Row>
          <Row style={{'marginTop':'40px', 'fontSize':'20px'}}>Min Words: <Input style={{'width':'100px', 'height':'50px', 'marginRight':'10px'}} value={this.state.min} placeholder='30' onChange={this.handleMinChange.bind(this)} />
          Max Words : <Input style={{'width':'100px', 'height':'50px'}} value={this.state.max} placeholder='100' onChange={this.handleMaxChange.bind(this)} /></Row>
          <Row style={{'marginTop':'25px'}}><Button style={{'fontSize': '22px'}} type='submit' onClick = {this.fetchData}>Search</Button></Row>
          { loading === true ? (

           <Loader active inline='centered'size='massive'>Loading</Loader>
         ) : (<div />) }
        </Form>
        <Row style={{'marginTop':'100px'}}>
          <Row>
            <Header size='huge'>Results</Header>
          </Row>
          { this.state.sysData === '' ? (<div/>) :
          (<Row><Tabs data={this.state.sysData}/></Row>)
          }
          </Row>
          <Row style={{marginTop:'22%'}}>Photo by <a href='https://unsplash.com/@samscrim' target='_blank'>Samuel Scrimshaw</a> on <a href='https://unsplash.com' target='_blank'>Unsplash</a></Row>
      </Row>
    )
  }
}
export default DetailsForm
