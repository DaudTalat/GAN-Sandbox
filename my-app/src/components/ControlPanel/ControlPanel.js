import React, { useState } from "react";
import "./ControlPanel.css";
import { Select, MenuItem } from "@mui/material";

const ControlPanel = () => {

  function train() {
    fetch("/train");
  }

  function generate() {
    fetch("/generate");
  }

  function get_photo(id) {
    fetch("/gen_images/" + id);
  }

  const [res, setRes] = useState("");

  const handleChange = (event) => {
    setRes(event.target.value);
  };

  return (
    <div class="control-panel">
      <div className="row">
        <div className="help-menu">
          <h1 className="control-help-h">Generating Images</h1>
          <p className="control-help-p">
            To initiate the training process, choose and train a set of images.
            Once the training is complete, you can generate 5 photos for each
            generation.
          </p>
        </div>

        <div className="train">
          <h1 className="control-help-h">GAN Control</h1>

          <p style={{ color: "#696969" }} className="control-help-p">
            Train
          </p>

          <button className="button-style" onClick={train}>Train Model</button>

          <p style={{ color: "#696969" }} className="control-help-p">
            Generate
          </p>

          <button className="button-style" onClick={generate}>Generate</button>
        </div>
      </div>

      <div className="resolution">
        <h1 className="control-help-h">Image Settings</h1>
        <p style={{ color: "#696969" }} className="control-help-p">
          Resolution
        </p>

        <Select className="select-res" value={res} onChange={handleChange}>
          <MenuItem value={1}>Ten</MenuItem>
          <MenuItem value={2}>Twenty</MenuItem>
          <MenuItem value={3}>Thirty</MenuItem>
        </Select>
      </div>
    </div>
  );
};

export default ControlPanel;
