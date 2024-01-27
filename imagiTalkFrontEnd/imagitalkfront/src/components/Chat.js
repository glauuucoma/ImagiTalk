import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import character from "../img/chat-char.png";
import NorthIcon from "@mui/icons-material/North";

const Chat = () => {
  return (
    <Container fluid className="chat">
      <Row>
        <Col lg={3} className="character-info">
          <div className="character-icon-wrapper">
            <div className="character-icon">
              <img src={character} alt="character" />
            </div>
            <p>Character name</p>
          </div>
          <div className="chat-history">
            <button className="chat-history-btn">Chat #{1}</button>
            <button className="chat-history-btn">Chat #{2}</button>
            <button className="chat-history-btn">Chat #{3}</button>
          </div>
          <button className="create-chat-btn">New chat</button>
        </Col>
        <Col lg={9} className="chat-input-wrapper">
          <p>
            Ask your favourite character
            <br />
            any question....
          </p>
          {/* <input type="text" placeholder="How are you doing?" />
           */}
          <form>
            <textarea />
            <button>
              <img src={NorthIcon} alt="icon" />
            </button>
          </form>
        </Col>
      </Row>
    </Container>
  );
};

export default Chat;
