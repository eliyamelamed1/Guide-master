// 3 : data => context => FeaturedRooms => Room  => SingleRoom
// feature rooms section in the bottom of the Home page

import React, { Component } from 'react'
import { RoomContext } from '../context'
import Loading from './Loading';
import Room from './Room';
import Title from './Title'; 

export default class FeaturedRooms  extends Component {
    static contextType = RoomContext;
    render() {
        let { loading, featuredRooms } = this.context; // a remainder that in es6 let/const {variable} = this.something , is the same as let variable = this.something.variable
        
        // Passing the featuredRooms objects to the Room componnent
        // the Room component template page - that get room props and turn it into a visual room card (display image, price, name)
        // at last featuredRooms = visual featuredRooms cards (display image, price, name)
        featuredRooms = featuredRooms.map(room => {
            return ( 
                <Room // passing props (data) to Room Component and calling that function
                key={room.id} 
                room={room}/>
            )
        });

        return (
            // Return the Featured room section
            <section className="featured-rooms container">
                <Title  title="Featured Rooms" />
                <div className="row">
                  {loading ? <Loading/> : featuredRooms} {/* if loading property is true ( true = data is loading )  display the Loading component , else display featured rooms */}
                </div>
            </section>
        )
    }
}

