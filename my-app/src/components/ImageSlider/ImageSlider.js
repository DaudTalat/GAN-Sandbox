import { useEffect, useState } from "react";
import "./ImageSlider.css";

const ImageSlider = ({ slides }) => {
  const [currIndex, setIndex] = useState(0);

  const sliderPos = {
    height: "100%",
    position: "relative",
    marginTop: "50px"
  };

  const slider = {
    /* Cannot pass into .css file */ 
    width: "100%",
    height: "100%",
    borderRadius: "20px",
    backgroundPosition: "center",
    backgroundSize: "cover",
    backgroundImage: `url(${slides[currIndex].url})`,
    border: "3px solid #2D8FFF",
    transition: "background-image 0.5s ease-in-out", // CSS transition
  };

  const moveBack = () => {
    let firstSlide;
    let backIndex;

    if (currIndex === 0) {
      firstSlide = true;
    } else {
      firstSlide = false;
    }

    if (firstSlide) {
      backIndex = slides.length - 1;
    } else {
      backIndex = currIndex - 1;
    }

    setIndex(backIndex);
  };

  const moveForward = () => {
    let lastSlide;
    let forwardIndex;

    if (currIndex === slides.length - 1) {
      lastSlide = true;
    } else {
      lastSlide = false;
    }

    if (lastSlide) {
      forwardIndex = 0;
    } else {
      forwardIndex = currIndex + 1;
    }

    setIndex(forwardIndex);
  };

  const moveToSlide = (index) => {
    setIndex(index);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prevIndex) =>
        prevIndex === slides.length - 1 ? 0 : prevIndex + 1
      );
    }, 5000);

    return () => clearInterval(interval);
  }, [currIndex]);

  return (
    <div style={sliderPos}>
      <div style={slider}></div>
      <div className="radio-container">
        {slides.map((slide, index) => (
          <div
            key={index}
            className={`radio ${index === currIndex ? "active" : ""}`} /* define value as "active" for index */
            onClick={() => moveToSlide(index)}
          >
            ●
          </div>
        ))}
      </div>
    </div>
  );
};

export default ImageSlider;
