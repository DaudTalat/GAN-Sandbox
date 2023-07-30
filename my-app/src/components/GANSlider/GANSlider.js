import React, { useState, useEffect } from "react";
import "./GANSlider.css";

const GANSlider = (count) => {

  const [img1, setImg1] = useState('');
  const [img2, setImg2] = useState('');
  const [img3, setImg3] = useState('');
  const [img4, setImg4] = useState('');
  const [img5, setImg5] = useState('');
  const [selectedPhoto, setSelectedPhoto] = useState(null);

  useEffect(() => {
    // Fetch Image 1
    fetch("/gen_images/" + 0)
      .then(response => response.blob())
      .then(blob => {
        const img1 = URL.createObjectURL(blob);
        setImg1(img1);
        setSelectedPhoto(img1) // Set our Main Photo
      });

    // Fetch Image 2 
    fetch("/gen_images/" + 1)
      .then(response => response.blob())
      .then(blob => {
        const img2 = URL.createObjectURL(blob);
        setImg2(img2);
      });


    // Fetch Image 3
    fetch("/gen_images/" + 2)
      .then(response => response.blob())
      .then(blob => {
        const img3 = URL.createObjectURL(blob);
        setImg3(img3);
      });

    // Fetch Image 4
    fetch("/gen_images/" + 3)
      .then(response => response.blob())
      .then(blob => {
        const img4 = URL.createObjectURL(blob);
        setImg4(img4);
      });

    // Fetch Image 5
    fetch("/gen_images/" + 4)
      .then(response => response.blob())
      .then(blob => {
        const img5 = URL.createObjectURL(blob);
        setImg5(img5);
      });

  }, [count]);


  const selectPhoto = (photo) => {
    setSelectedPhoto(photo);
  };


  return (
    <div>
      <div className="selector-container">
        <img
          className="gen-image"
          src={selectedPhoto}
          alt="Large Photo"
        />
      </div>

      <div className="selector-container">
        <img
          className={`thumbnail ${selectedPhoto === img1 ? 'selected' : ''}`}
          src={img1}
          alt="thumb-1"
          onClick={() => selectPhoto(img1)}
        />
        <img
          className={`thumbnail ${selectedPhoto === img2 ? 'selected' : ''}`}
          src={img2}
          alt="thumb-2"
          onClick={() => selectPhoto(img2)}
        />
        <img
          className={`thumbnail ${selectedPhoto === img3 ? 'selected' : ''}`}
          src={img3}
          alt="thumb-3"
          onClick={() => selectPhoto(img3)}
        />
        <img
          className={`thumbnail ${selectedPhoto === img4 ? 'selected' : ''}`}
          src={img4}
          alt="thumb-4"
          onClick={() => selectPhoto(img4)}
        />
        <img
          className={`thumbnail ${selectedPhoto === img5 ? 'selected' : ''}`}
          src={img5}
          alt="thumb-5"
          onClick={() => selectPhoto(img5)}
        />
      </div>
    </div>
  );
};

export default GANSlider;
