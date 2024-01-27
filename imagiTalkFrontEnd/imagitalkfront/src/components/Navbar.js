import React from 'react';
import { Navbar as BootstrapNavbar, Nav } from 'react-bootstrap';
import LogoImage from '../img/logo.png';  // Import the logo image

const Navbar = () => {
  return (
    <BootstrapNavbar className='navbar justify-content-between'>
      <BootstrapNavbar.Brand className=''>
        <img
          alt="Logo"
          src={LogoImage}  // Use the imported image directly
          className="d-inline-block align-top logo"
        />
      </BootstrapNavbar.Brand>
      <Nav className="">
        <Nav.Link className='text-white'>
          HOME
        </Nav.Link>
        <Nav.Link className='text-white'>
          SIGN IN
        </Nav.Link>
        <Nav.Link className='text-white'>
          LOGIN
        </Nav.Link>
      </Nav>
    </BootstrapNavbar>
  );
};

export default Navbar;