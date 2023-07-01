import React from 'react'
import ImageSlider from '../../components/ImageSlider/ImageSlider';
import Hero from "../../components/Hero/Hero";
import './Home.css'

const Home = () => {
    const multiple_slides = [
        {url: "https://static01.nyt.com/images/2019/03/27/arts/26VANGOGH-BRITAIN-1/merlin_152403333_3552f80f-9675-4951-bc32-0b8cbdbfa090-superJumbo.jpg", title: "Van Gogh"},
        {url: "https://d7hftxdivxxvm.cloudfront.net/?height=599&quality=80&resize_to=fit&src=https%3A%2F%2Fd32dm0rphc51dk.cloudfront.net%2F_-aKbmh7pS23sONnmvB4yQ%2Fnormalized.jpg&width=800", title: "Bob Ross"},
        {url: "https://en.most-famous-paintings.com/Art.nsf/O/5ZKELQ/$File/Rene_Magritte-The_Human_Condition.jpg", title: "Rene Magritte"}
    ];

    const containerStyle = {
        width: "550px",
        height: "550px",
        margin: '0',
    };


    return (
        <>
            <div className="home-container">
                <div style={containerStyle}>
                    <ImageSlider slides={multiple_slides} />
                </div>

                <Hero/>
            </div>
        </>
    );
};

export default Home