import React from 'react';
import './Hero.css';

const Hero = () => {
  return (
    <>
      <div className="hero-container">
        <h1 className="heading">Imagine. Generate. Create. Innovate.</h1>
        <div className="description">
          <div className="blue-bar"></div>
          <p>
          <span style={{fontWeight: 600}}>Discover Sandbox:</span> where AI generates captivating visuals in a limitless creative sandbox. Unleash your artistic potential with customizable image sets. Inspire innovation.
          </p>
          <div className="buttons">
            <a href="/start" className="rounded-button">Use Local Machine</a>
            <a href="https://colab.research.google.com/drive/1fUyse9L1EWpCv04XaFRv-Jr9snFkWVBt?usp=sharing" className="rounded-button">Use Google Colab</a>
          </div>
        </div>
      </div>
    </>
  );
};

export default Hero;