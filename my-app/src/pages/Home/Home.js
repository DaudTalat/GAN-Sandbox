import React from 'react'
import ImageSlider from '../../components/ImageSlider/ImageSlider';
import Hero from "../../components/Hero/Hero";
import "./Home.css";

// art
import gogh from "../../assets/images/gan1.png";
import ross from "../../assets/images/gan2.png";
import ivan from "../../assets/images/gan3.png";

const Home = () => {
    const multiple_slides = [
        {url: gogh, title: "gan1"},
        {url: ross, title: "gan2"},
        {url: ivan, title: "gan3"}
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