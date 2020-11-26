// 4 : data => context => FeaturedRooms => Room  => SingleRoom
// Room template page - gets room props and turn it into a visual room card (display image, price, name)

import React from 'react';
import {Link} from 'react-router-dom';
import defaultImg from '../images/room-1.jpeg';
import PropTypes from 'prop-types';

export default function Room({room}) {
    const { name , slug, images, price } = room; // a remainder that in es6 let {variable} = this.context , is the same as let variable = this.context.variable
    return (
        <div className="col-md-4 col-12 mx-auto p-2">
            <div className="card shadow-lg border-0 room">
                
                <img src={images[0] || defaultImg} alt="single room" className="img-fluid"/> {/* Display the first image of a room images array, if there is a problem with the image load a default image*/}
                
                <div className="price-top">
                    <h6>$ {price}</h6> {/* set room price base on the room price property*/}
                    <p>per night</p>
                </div>

                
                <Link to={`/rooms/${slug}`} className="btn-warning room-link text-center" >Features</Link> {/* Linking each room to a unique url based on his slug property {room.slug} */}
              
              <p className="room-info">{name}</p> {/* Display the room name on the room card*/}
            </div>
        </div>
    )
}


// Not A Must But Good To Have
// method to check props passed to your components against those definitions, and warn in development if they don’t match. 
Room.propTypes = {
    room: PropTypes.shape({
        name:PropTypes.string.isRequired,
        slug:PropTypes.string.isRequired,
        images:PropTypes.arrayOf(PropTypes.string).isRequired,
        price:PropTypes.number.isRequired,
    })
}
