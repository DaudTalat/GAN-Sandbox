import {React} from "react";
import "./About.css"



const About = () => {

    document.body.style = "background: #fff";

    return (


        <div className="about-container">

            <div className="group-about">

                <h1 className="about-heading">
                    About
                </h1>

                <p1 className="about-paragraph">
                This honours project exhibits a generative adversarial network (GAN) environment directed to providing users with increased control and security of their own data with respect to image modelling training. Historic limitations have made GAN practices inaccessible. For instance, the constrained nature of compounded datasets and computational resources. As conditions improve, with the advancements in graphics processing units, coupled with the emergence of data science communities such as Kaggle, the proposed environment becomes viable, presenting an innovative solution. The GAN Sandbox is outfitted with an intuitive user interface which conceals the model's intricate underlying logic. By this design, essential features are abstracted, including image processing, routing, and model checkpointing. The platform enables both developers and artists alike to independently train GANs on their own hardware, utilizing custom datasets to explore a multitude of creative ventures in image generation. The application of this project can extend to many domains ranging from computer vision to creative arts.                  </p1>
            </div>


            <div className="group-acknowledgements">
                <h1 className="about-heading">
                    Acknowledgements
                </h1>

                <p1 className="about-paragraph">
                I would like to take this opportunity to express my heartfelt gratitude to all those who have contributed to the successful completion of my honours project. This achievement would not have been possible if it were not for the enduring support I have received from various individuals—continuously giving me both invaluable guidance and assistance.                 </p1>
                <br/>
                <p1 className="about-paragraph">
                First and foremost, I want to extend my sincere appreciation to my esteemed professor, Dave McKenney, for his continued support, mentorship, and expertise. The dedication he has to teaching as well as fostering a learning environment has been instrumental through the progression of this project.
                </p1>
                <br/>
                <p1 className="about-paragraph">
                I am also indebted to my fellow classmates, who provided me with encouragement and understanding. Their eagerness to discuss ideas relating to the usability of the project inspired its course and enriched the overall development process.
                </p1>
            </div>
        </div>
    )
}

export default About;