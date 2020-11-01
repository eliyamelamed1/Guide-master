import React from 'react'
import Hero from '../components/Hero'
import Banner from '../components/Banner';
import { Link } from 'react-router-dom';
import RoomsContainer from '../components/RoomsContainer';
const Rooms = () => {
    return (
    <div>
        {/* passing props to all the components */}
        <Hero hero="roomsHero" /> {/* Content */}  
        <Banner title="Available Rooms" subtitle="Best in Class Room"> {/* Banner */}
                <Link to="/" className="btn btn-warning"> RETURN HOME </Link> {/* Button */}
        </Banner>
        <RoomsContainer/> {/* Rooms Container */}
    </div>
    )
}

export default Rooms
