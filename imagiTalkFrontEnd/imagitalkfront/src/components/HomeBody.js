import { Container, Row, Col, Button } from 'react-bootstrap';

const HomeBody = () => {
    return (<>
        <Container fluid className="m-5 home-body">
            <Row className="home-body-text-block">
                <Col md={7} className="pl-5">
                    <h1 className="custom-header">Chat with your</h1> 
                    <h1 className="custom-header">favourite character</h1>
                    <h1 className="custom-header">from the past</h1>
                    <p>Just type out the name of the character you want to <br/> talk to and explore the endless possibilities of<br/> interactive storytelling</p>
                    <Button className="start-chatting-btn px-5 mt-2">CHAT</Button> 
                </Col>
            </Row>  
        </Container>
    </>)
}
export default HomeBody;