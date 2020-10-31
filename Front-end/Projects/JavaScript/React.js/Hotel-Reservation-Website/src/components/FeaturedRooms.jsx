// 3 : data => context => FeaturedRooms 
import React, { Component } from 'react'
import { RoomContext } from '../context'
import Loading from './Loading';
import Room from './Room';
import Title from './Title'; 

export default class FeaturedRooms  extends Component {
    static contextType = RoomContext;
    render() {
        let { loading, featuredRooms } = this.context; // a remainder that in es6 let {loading} = this.context , is the same as let loading = this.context.loading  and featuredRooms : rooms , is the same as rooms = featuredRooms
        featuredRooms = featuredRooms.map(room => {
            return <Room key={room.id} room={room}/> // passing props (data) to Room Component
        });
        return (
 
            <section className="featured-rooms container">
                <Title  title="Featured Rooms" />
                <div className="row">
                  {loading ? <Loading/> : featuredRooms} {/* if loading property ( he is true when the data finish loading ) is true display the Loading component , else display featured rooms */}
                </div>
            </section>
        )
    }
}

