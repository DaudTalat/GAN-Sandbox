import React, { useEffect, useState } from 'react';

const GeneratedImage = (props) => {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    fetch("/gen_images/" + props.id)
      .then(response => response.blob())
      .then(blob => {
        const objectURL = URL.createObjectURL(blob);
        setImageUrl(objectURL);
      });
  }, []);

  return (
    <>
      <img src={imageUrl} alt="Press Generate to Get Started." />
    </>
  );
};

export default GeneratedImage;