import { Container, Row, Col, Button } from 'react-bootstrap';

const HomeBody = () => {
    return (<>
        <Container fluid className="mt-5 home-body">
            <Row>
            <Col md={7} className="pl-5">
                <h1 class="custom-header">Chat with you favourite character from the past</h1>
                <p>Just type out the name of the character you want to talk to and explore the endless possibilities of interactive storytelling</p>
                <Button className="home-button">Click me</Button>
            </Col>
            </Row>
        </Container>
    </>)
}

export default HomeBody;