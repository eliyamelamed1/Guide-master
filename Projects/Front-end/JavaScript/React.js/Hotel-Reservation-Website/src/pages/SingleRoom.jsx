// 5 : data => context => FeaturedRooms => Room  => SingleRoom


import React, { Component } from 'react'
import defaultBcg from '../images/room-3.jpeg';
import Banner from '../components/Banner';
import { Link } from 'react-router-dom';
import { RoomContext } from '../context';
import StyledHero from '../components/StyledHero';

export default class SingleRoom extends Component {
    constructor (props){
        super(props);
        this.state = {
            slug: this.props.match.params.slug, // TODO----- LEARN ABOUT this.props.match.params
            defaultBcg // default image
        };
    }

    static contextType = RoomContext;

    render() {
        const { getRoom } = this.context; // saving the getRoom function into a variable
        const room = getRoom(this.state.slug); // match between the room and the slug

        // if room slug link is undefined (doesnt exist)
        // show error page
        if(!room){
            return (<div className="container roomerror">
                    <div className="row my-5">
                        <div className="col-md-6 col-12 mx-auto">
                            <div className="card shadow-lg border-0 p-4 error">
                                <h1 className="text-center display-4">SORRY</h1>
                                <h3>No such room could be found...</h3>
                                <Link to="/rooms" className="btn btn-warning mt-4 ">Back to Rooms</Link>
                            </div> 
                        </div>
                    </div>
                </div>);
        }

        
        const {name,description,capacity,size,price,extras,breakfast,pets,images} = room; // a remainder that in es6 let/const {variable} = this.something , is the same as let variable = this.something.variable
        const [mainImg, ...defaultBcg] = images;
        return (
            <>
            {/* ROOMS IMG */}
                <StyledHero img={mainImg || this.state.defaultBcg }> {/* load first img , if it isnt available load the second img (default image) [NOTE: look at StyledHero component for more info] */}

                    <Banner title={`${name} room`}> {/* load banner with room.name */}

                            <Link to="/rooms" className="btn btn-primary">Back To Rooms</Link> { /* Button on the banner */ }

                    </Banner>
                </StyledHero>

                
                <section className="single-room container">
                <div className="row">
                        {defaultBcg.map((image,index) => {
                            return (
                            <div className="col-md-4 col-12 mx-auto" > {/* I removed key={index} from className*/}
                                <div className="card border-0 shadow-lg">
                                <img key={index} src={image} alt={name} className="img-fluid" />
                                </div>
                            </div>)
                        })}
                </div>
                <div className="single-room-info">
                    <article className="desc">
                        <h3>Details</h3>
                        <p>{description}</p>
                    </article>
                    <article className="info">
                        <h3>Info</h3>
                        <h6>price : ${price}</h6>
                        <h6>size  : {size} SQFT</h6>
                        <h6>
                            max capacity : {" "}
                                {capacity > 1 ? `${capacity} people`: `${capacity} person`}
                        </h6>
                        <h6>{pets? 'pets allowed': 'no pets allowed'}</h6>
                        <h6>{breakfast && "free breakfast included"}</h6>
                    </article>
                </div>
                </section>
                <section className="room-extras">
                    <h3>Extras</h3>
                    <ul className="extras">
                        {extras.map((item,index) => {
                            return <li key={index}>{item}</li>
                        })}
                    </ul>
                    <div className="p-4 clearfix">
                        <div className="row">
                        <div className="col-md-3 col-12 ml-auto">
                            <Link to={`/booknow/${this.state.slug}`} className="btn btn-outline-primary btn-block btn-lg float-right ">Book Now</Link>
                        </div>
                        </div>
                    </div>
                </section>
            </>
        )
    }
}
