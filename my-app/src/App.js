import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import React from 'react';

function App() {

  function train () {
    fetch('/train')
  }

  function generate () {
    fetch('/generate')
  }

  return (
    <div className="App">
        <header className="App-header">
        </header>
        <Button
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
    </div> 
  );
}

export default App;
