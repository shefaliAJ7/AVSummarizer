import React from 'react'
import { Tab, Form, Comment, Table} from 'semantic-ui-react'


import ReactPlayer from 'react-player'

import { Row, Layout, Col, Card,  Menu, Breadcrumb, Carousel } from 'antd';

import userImg from "../assets/img/user.png"
import _ from 'lodash'


class Tabs extends React.Component {

  render(){

        return (<div> <Table celled>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>Text</Table.HeaderCell>
        <Table.HeaderCell>Summary</Table.HeaderCell>
      </Table.Row>
    </Table.Header>

    <Table.Body>
      <Table.Row>

        <Table.Cell>Cell</Table.Cell>
        <Table.Cell>Cell</Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell>Cell</Table.Cell>
        <Table.Cell>Cell</Table.Cell>

      </Table.Row>

    </Table.Body>
    </Table>
</div>);
  }
}
export default Tabs
