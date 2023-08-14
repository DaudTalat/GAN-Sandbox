import React, { useState } from "react";
import "./ControlPanel.css";
import { Select, MenuItem } from "@mui/material";

const ControlPanel = ({ onClick }) => {
  const [isTraining, setIsTraining] = useState(false)

  function toggleTraining() {
    fetch("/train");
    setIsTraining(!isTraining); // Toggle training status
  }

  function generate() {
    fetch("/generate")
      .then((response) => {
        if (!response.ok) {
          throw new Error(
            "There is an issue with your back-end, or filesystem."
          );
        }
        return response.json(); // Assuming the response is in JSON format
      })
      .then((data) => {
        console.log(data);
        onClick();
      });
  }

  function get_photo(id) {
    fetch("/gen_images/" + id);
  }

  const [res, setRes] = useState(1);

  const handleChange = (event) => {
    setRes(event.target.value);
    if (res == 1) {
      fetch("/setres/HR")
    } else {
      fetch("/setres/SR")
    }
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

          <button className="button-style" onClick={toggleTraining}>
            {isTraining ? "Stop Training": "Start Training"}
          </button>

          <p style={{ color: "#696969" }} className="control-help-p">
            Generate
          </p>

          <button
            className="button-style"
            onClick={() => {
              generate();
            }}
          >
            Generate
          </button>
        </div>
      </div>

      <div className="resolution">
        <h1 className="control-help-h">Image Settings</h1>
        <p style={{ color: "#696969" }} className="control-help-p">
          Resolution
        </p>

        <Select className="select-res" value={res} onChange={handleChange}>
          <MenuItem value={1}>128x128 - Standard Resolution</MenuItem>
          <MenuItem value={2}>256x256 - High Resolution</MenuItem>
        </Select>
      </div>
    </div>
  );
};

export default ControlPanel;
