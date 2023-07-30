import { React, useState } from "react";
import "./Start.css";

import ControlPanel from "../../components/ControlPanel/ControlPanel";
import GeneratedImage from "../../components/GeneratedImage/GeneratedImage";
import GANSlider from "../../components/GANSlider/GANSlider";
import CheckpointPanel from "../../components/CheckpointPanel/CheckpointPanel";

const Start = () => {

  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  document.body.style = "background: #fff";

  return (
    <div className="start-container">
      <ControlPanel onClick={handleClick}/>

      <div className="start-heading-group">
        <h1 className="start-heading">AI Image Generator.</h1>
        <p1 className="start-paragraph">
          Retrieve AI-generated images from a collection of visual data directly
          within your web browser.
        </p1>

        <GANSlider />
      </div>

      <CheckpointPanel count={count}/>
    </div>
  );
};

export default Start;
