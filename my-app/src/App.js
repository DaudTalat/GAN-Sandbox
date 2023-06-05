import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react';

function App() {

  function buttonClick () {
    fetch('/dauds')
  }

  return (
    <div className="App">
        <header className="App-header">
        </header>
        <p>blank</p>
        <Button
          variant='outlined'
          color='secondary'
          onClick={buttonClick}
        >
          Barry Berkman
        </Button>
    </div> 
  );
}

export default App;
