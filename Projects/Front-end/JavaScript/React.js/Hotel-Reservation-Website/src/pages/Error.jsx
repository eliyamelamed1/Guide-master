import React from 'react'
import Hero from '../components/Hero'
import Banner from '../components/Banner';
import { Link } from 'react-router-dom';
import {FaRegMeh} from 'react-icons/fa';

export default function Error() {
    return (
        <>
        {/* passing props to all the components */}
        <Hero hero="roomsError" /> {/* passing props to Hero component */} {/* Image */}
        <Banner title="ERROR 404 NOT FOUND" subtitle="You are lost !! ITs dark everywhere"> {/* passing props to Banner component */} {/* Banner Component */}
                <FaRegMeh className="lost" /> {/* smiley icon */}
                <Link to="/" className="btn btn-warning"> RETURN HOME </Link> {/* Button */}
        </Banner>
        </>
    )
}
