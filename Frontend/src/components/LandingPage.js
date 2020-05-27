import React from 'react';
import mapImage from './../assets/img/map.png';
import { Row, Layout, Col, Card,  Menu, Breadcrumb, Carousel} from 'antd';
import {Image, Divider} from 'semantic-ui-react';
import StyledFirebaseAuth from "react-firebaseui/StyledFirebaseAuth"
import firebase from "firebase"

class LandingPage extends React.Component {
    constructor(props){
        super(props);
        this.state={}
    }
    render(){
        return(
            <div style={{backgroundImage:"url(" + mapImage + ")", padding:'15%', backgroundPosition: 'center',backgroundSize: 'cover',backgroundRepeat: 'no-repeat'}}>

                    <StyledFirebaseAuth
                        uiConfig={this.props.uiConfig}
                        firebaseAuth={this.props.firebaseAuth}
                    />
                    <div style={{ marginTop:'10%', color:'white', fontSize:'85px',
                                fontFamily:'"Ariel", Helvetica, sans-serif', textAlign:'center'}}>
                        AV SUMMARIZER


                </div>
                <Row style={{marginTop:'32%', color:'white'}}>Photo by <a href='https://unsplash.com/@andrew_haimerl' target='_blank'>Andrew Haimerl</a> on <a href='https://unsplash.com' target='_blank'>Unsplash</a></Row>
            </div>
        );
    }
}
export default LandingPage;
