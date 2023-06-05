import React from 'react'
import { Link, Router } from 'react-router-dom'
import { Button } from '@mui/material'

function RoutedButton () {
    return (
        <Link>
            <Button variant='contained' color='primary'>
                Barry Berkman
            </Button>   
        </Link>
    );
};


export default RoutedButton;