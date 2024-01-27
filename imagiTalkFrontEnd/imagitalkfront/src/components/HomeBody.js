import { Container, Row, Col, Button } from 'react-bootstrap';

const HomeBody = () => {
    return (<>
        <Container fluid className="m-5 home-body">
            <Row className="home-body-text-block">
                <Col md={7} className="pl-5">
                    <h1 className="custom-header">Chat with you favourite character from the past</h1>
                    <p>Just type out the name of the character you want to talk to and explore the endless possibilities of interactive storytelling</p>
                </Col>
            </Row>  
            <Row>
                <Col>
                    <div className='btn-div'>
                        <Button className="start-chatting-btn">CHAT</Button>
                    </div>  
                </Col>
            </Row>
        </Container>
    </>)
}
export default HomeBody;