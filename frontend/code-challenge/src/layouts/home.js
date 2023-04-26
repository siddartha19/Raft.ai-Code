import React, { Component } from "react";
import { Image, Spin } from 'antd';
import axios from 'axios';
import CardGrid from "./drag";

class Home extends Component {

    state = {
        myData: [],
    }

    componentDidMount () {
        axios.get('http://localhost:8000/')
            .then((response) => {
                this.setState({ myData: response.data.data });
            })
    }
  
    render () {
        return (<>
            <div style={{ margin: "40px 50px", display: "flex", flexWrap: "wrap", justifyContent: "center" }}>
                {this.state.myData.map( (item) => (
                    <div style={{ flex: "0 0 calc(30% - 20px)" }}>
                        <p>{item['title']}</p>
                        <div >
                            <Image
                                width={200}
                                src="https://images6.alphacoders.com/337/337780.jpg"
                                placeholder={<Spin />}
                            />
                        </div>
                    </div>
                ))}
            </div>
            
            {/* tried draggable card grid, but couldn't make it */}
            {/* <CardGrid /> */}
        </>);
    }
}


export default Home;
