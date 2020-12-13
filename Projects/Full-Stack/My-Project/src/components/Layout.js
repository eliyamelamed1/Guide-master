import React from 'react';
import Navbar from './NavBar';

const Layout = (props) => (
  <div>
    <Navbar />
    {props.children}
  </div>
);

export default Layout;
