import React from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";

const Chat = () => {
  return (
    <Container fluid>
      <Row>
        {/* First column */}
        <Col md={3} style={{ background: "#F77B63", padding: "20px" }}>
          {/* Image and description */}
          <div>
            <img
              src="https://placekitten.com/150/150" // Replace with your image URL
              alt="User Avatar"
              style={{ width: "100%", borderRadius: "50%" }}
            />
          </div>
          <div style={{ marginTop: "10px" }}>
            <p>Description goes here</p>
          </div>

          {/* Buttons */}
          <div style={{ marginTop: "20px" }}>
            <Button variant="outline-light" block>
              Button 1
            </Button>
            <Button variant="outline-light" block>
              Button 2
            </Button>
            <Button variant="outline-light" block>
              Button 3
            </Button>
          </div>

          {/* Full-width button */}
          <div style={{ marginTop: "20px" }}>
            <Button variant="danger" block>
              Big Button
            </Button>
          </div>
        </Col>

        {/* Second column */}
        <Col md={9} style={{ padding: "20px" }}>
          {/* Input form */}
          <Form>
            <Form.Group controlId="formMessage">
              <Form.Control type="text" placeholder="Type your message..." />
            </Form.Group>
            <Button variant="primary" type="submit" block>
              Submit
            </Button>
          </Form>

          {/* Text in the center */}
          <div style={{ textAlign: "center", marginTop: "20px" }}>
            <p>Text in the center</p>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default Chat;
