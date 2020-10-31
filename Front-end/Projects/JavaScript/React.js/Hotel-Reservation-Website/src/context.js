// 2 : data => context
import React, { Component } from 'react'
import items from './data'; // you can use everyname you want instead of items

const RoomContext = React.createContext();


export default class RoomProvider extends Component {
    // Creating Components
    state={
        rooms: [], // all the rooms 
        sortedRooms: [], // rooms after filter [rooms => search rooms]
        featuredRooms: [], // featured rooms in the bottom of home page [home => featured rooms] 
        loading: true,
        type: 'all',
        capacity: 1,
        price: 0,
        minPrice: 0,
        maxPrice: 0,
        minSize: 0,
        maxSize: 0,
        breakfast: false,
        pets: false
    };

    
    componentDidMount(){
        let rooms = this.formatData(items); // Saving the accessed data into a variable
        let featuredRooms = rooms.filter(room => room.featured === true); // each item have featuredRoom property equal to True/False, if the property equal to True he will be added to the array
        let maxPrice = Math.max(...rooms.map(item => item.price)); // function to save the highest price into a variable
        let maxSize = Math.max(...rooms.map(item => item.size)); // function to save the lowest price into a variable
        
        // modify the data
        this.setState({
            rooms, // rooms , is the same as rooms: rooms in es6
            featuredRooms,
            sortedRooms:rooms,
            loading: false,
            price : maxPrice,
            maxPrice,
            maxSize
        })
    }
    
    // Accessing data
    formatData(items){
        let tempItems = items.map(item =>{
        let id = item.sys.id;
        let images = item.fields.images.map(image => image.fields.file.url);
        let room = {...item.fields,images,id}
        return room;    
        });
        return tempItems;
    }

    getRoom = (slug) => {
        let tempRooms = [...this.state.rooms];
        const room = tempRooms.find((room)=>room.slug === slug);
        return room;
    }

    handleChange = event => {
        const target = event.target;
        const value = target.type ==='checkbox' ? target.checked:target.value;
        const name = event.target.name;
        this.setState(
        {
            [name]: value
        },this.filterRooms)
    }
    
    filterRooms = () => {
        let{
            rooms,type,capacity,price,minSize,maxSize,breakfast,pets
        }= this.state
        // for all the rooms
        let tempRooms = [...rooms];

        //transform value
        capacity = parseInt(capacity)
        price = parseInt(price)

        //filter by type
        if(type !=='all'){
            tempRooms = tempRooms.filter(room => room.type === type)
        }
        //filter by capacity
        if(capacity !==1){
            tempRooms = tempRooms.filter(room => room.capacity >= capacity)
        }
        //filter by price
        tempRooms = tempRooms.filter(room => room.price <= price);
        
        //filter by size
        tempRooms = tempRooms.filter(room => room.size >= minSize && room.size <= maxSize)

        //filter by breakfast
        if(breakfast){
            tempRooms = tempRooms.filter(room => room.breakfast === true)
        }
        //filter by pets
        if(pets){
            tempRooms = tempRooms.filter(room => room.pets === true)
        }
        //change state
        this.setState({
            sortedRooms: tempRooms
        })
    }
    render() {
        return (
            // a remainder that RoomContext was defined at the top of the page
            <RoomContext.Provider value={{ ...this.state, getRoom: this.getRoom ,handleChange: this.handleChange }}> {/* Passing data to {FeaturedRooms component} */}
                {this.props.children}
            </RoomContext.Provider>
        )
    }
}

const RoomConsumer = RoomContext.Consumer;

export function withRoomConsumer(Component){
    return function ConsumerWrapper(props){
        return <RoomConsumer>
            {value => <Component {...props} context={value} />}
        </RoomConsumer>
    }
}

export{RoomProvider,RoomConsumer,RoomContext}
     