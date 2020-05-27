import React from 'react';
import PropTypes from 'prop-types';
import { Button, Input, Icon, Col, Card } from 'antd';

const LoginForm = ({ handleSubmit }) => {
  let username;
  let password;

  const submit = (e) => {
    e.preventDefault();
    handleSubmit(username.input.value, password.input.value);
  };

  return (
    <Col
      xs={20}
      sm={16}
      md={10}
      lg={6}
    >
      <Card title="Login">
        <Col>
          <Input
            placeholder="E-mail"
            ref={(user) => {
              username = user;
              return username;
            }}
            prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />}
          />
        </Col>
        <Col style={{ marginTop: '20px' }}>
          <Input
            placeholder="Password"
            ref={(pass) => {
              password = pass;
              return password;
            }}
            type="password"
            onPressEnter={submit}
            prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />}
          />
        </Col>
        <Col style={{ marginTop: '20px' }}>
          <Button type="primary" onClick={submit}> Log in </Button>
        </Col>
      </Card>
    </Col>
  );
};

LoginForm.propTypes = {
  handleSubmit: PropTypes.func.isRequired,
};

export default LoginForm;
