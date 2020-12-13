import React from 'react';
import Navbar from './NavBar';

const Layout = (props) => {
  return (
    <div>
      <Navbar />
      {props.children}
    </div>
  );
};

export default Layout;
