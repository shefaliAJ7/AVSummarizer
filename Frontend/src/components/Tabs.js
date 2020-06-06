import React from 'react'
import { Tab, Form, Comment, Table} from 'semantic-ui-react'

import { Row, Layout, Col, Card,  Menu, Breadcrumb, Carousel } from 'antd';

import userImg from "../assets/img/user.png"
import _ from 'lodash'


class Tabs extends React.Component {

  render(){

  return (
    <div>
      <Table celled padded style={{"width":"100%"}}>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>Text</Table.HeaderCell>
        <Table.HeaderCell>Summary</Table.HeaderCell>
      </Table.Row>
    </Table.Header>

    <Table.Body>
      <Table.Row>

        <Table.Cell>{this.props.data.text}</Table.Cell>
        <Table.Cell style={{width:'350px'}}>{this.props.data.summary}</Table.Cell>
      </Table.Row>

    </Table.Body>
    </Table>
</div>);
  }
}
export default Tabs
