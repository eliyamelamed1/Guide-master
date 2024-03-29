import React from 'react'
import Hero from '../components/Hero';
import Banner from '../components/Banner';
import { Link } from 'react-router-dom';
import Services from '../components/Services';
import FeaturedRooms from '../components/FeaturedRooms';

export default function Home() {
    return (
        <>
        {/* passing props to all the components */}
        <Hero /> {/* Image */}
        <Banner title="Luxurious Rooms" subtitle="deluxe rooms starting at 299$"> {/* Banner Component */}
                <Link to="/rooms" className="btn btn-primary"> Our Rooms </Link> {/* Button */}
        </Banner>
        <Services/> {/* Services Componenet */}
        <FeaturedRooms/> {/* Featured Rooms Component */}
        </>

    )
}
