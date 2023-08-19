import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"

import "./App.css";
import Banner from "./components/Banner/Banner";
import NavBar from "./components/NavBar/NavBar";
import Home from "./pages/Home/Home";
import Start from "./pages/Start/Start";
import About from "./pages/About/About";

function App() {


  return (
    <div className="App">
      <header className="App-header"></header>

      <div className="container">
        <Banner />
        <NavBar />
          <Router>
            <Routes>
              <Route path="/" element={<Home/>} />
              <Route path="/start" element={<Start/>}/>
              <Route path="/about" element={<About/>}/>
            </Routes>
          </Router>
      </div>
    </div>
  );
}

export default App;
