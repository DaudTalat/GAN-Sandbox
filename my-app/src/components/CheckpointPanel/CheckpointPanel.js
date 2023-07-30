import { ClassNames } from "@emotion/react";
import { React, useState } from "react";
import { TextField } from "@mui/material";
import "./CheckpointPanel.css";

const CheckpointPanel = () => {

  const [modelName, setModelName] = useState('');

  const handleInputChange = (event) => {
    setModelName(event.target.value)
  }

  function sendCkptName() {
      fetch("/ckpt/" + modelName)
  };

  return (
    <div className="checkpoint-panel">
      <div className="row">
        <div className="checkpoint-menu">
          <h1 className="control-help-h">Loading Checkpoints</h1>
          <p className="control-help-p">
            To load checkpoints for generative art neural networks:
            <ol>
              <li>
                Enter the name of the model checkpoint (e.g., "BobRoss.h5 or VanGogh.ckpt").
              </li>
              <br />
              <li>Click the "Load" button to initiate the loading process. </li>
            </ol>
          </p>
          <p
            style={{ color: "#696969", marginTop: "40px"}}
            className="control-help-p"
          >
            Checkpoint Name
          </p>

          <div className="checkpoint-loading">
            <TextField
              className="checkpoint-input"
              label="Model-Name.h5"
              variant="outlined"
              value={modelName}
              onChange={handleInputChange}
            />

            <button className="load-button" onClick={sendCkptName}>Load</button>
          </div>

        </div>
      </div>
    </div>
  );
};

export default CheckpointPanel;
