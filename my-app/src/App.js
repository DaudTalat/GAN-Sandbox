import Button from "@mui/material/Button";
import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"

import "./App.css";
import Banner from "./components/Banner/Banner";
import NavBar from "./components/NavBar/NavBar";
import Home from "./pages/Home/Home";

function App() {

  function train() {
    fetch("/train");
  }

  function generate() {
    fetch("/generate");
  }

  function get_photo(id) {
    fetch("/gen_images/" + id);
  }

  return (
    <div className="App">
      <header className="App-header"></header>
      {/* <Button
          variant='outlined'
          color='primary'
          onClick={train}
          sx={{m: 3, mb:1, pr: 6.5}}
        >
          Train
        </Button>
        <br></br>
        <Button
          variant='outlined'
          color='secondary'
          onClick={generate}
          sx={{m: 3, mb:5}}
        >
          Generate
        </Button>
        <div className="Canvas-Photo">
          <GeneratedImage id="1" />
        </div> */}
      <div className="container">
        <Banner />
        <NavBar />
          <Router>
            <Routes>
              <Route path="/" element={<Home/>} />
            </Routes>
          </Router>
      </div>
    </div>
  );
}

export default App;
