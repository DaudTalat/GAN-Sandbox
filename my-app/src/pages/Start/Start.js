import React from 'react'
import './Start.css'

import ControlPanel from '../../components/ControlPanel/ControlPanel';
import GeneratedImage from '../../components/GeneratedImage/GeneratedImage';
import GANSlider from '../../components/GANSlider/GANSlider';
import CheckpointPanel from '../../components/CheckpointPanel/CheckpointPanel';

const Start = () => {

    document.body.style = 'background: #fff';


    return (
        <div className="start-container">

            <ControlPanel/>

            <div className='start-heading-group'>
                <h1 className="start-heading">AI Image Generator.</h1>
                <p1 className="start-paragraph">Retrieve AI-generated images from a collection of visual data directly within your web browser.</p1>

                <GANSlider />
            </div>

            <CheckpointPanel/>

        </div>
    );
};

export default Start