import React from 'react'
import ImageSlider from '../../components/ImageSlider/ImageSlider';
import Hero from "../../components/Hero/Hero";
import "./Home.css";

// art
import gogh from "../../assets/images/vangogh.jpg";
import ross from "../../assets/images/bobross.png";
import monet from "../../assets/images/claudemonet.jpg";

const Home = () => {
    const multiple_slides = [
        {url: gogh, title: "Van Gogh"},
        {url: ross, title: "Bob Ross"},
        {url: monet, title: "Claude Monet"}
    ];

    const containerStyle = {
        width: "550px",
        height: "550px",
        margin: '0',
    };
    
    return (
        <body>
            <div className="home-container">
                <div style={containerStyle}>
                    <ImageSlider slides={multiple_slides} />
                </div>
                <Hero/>
            </div>
        </body>
    );
};

export default Home