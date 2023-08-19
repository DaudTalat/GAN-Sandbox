# GAN-Sandbox

The GAN Sandbox environment is a interactive web-application configured to allow users to generate artistic images using the power of Generative Adversarial Networks (GANs). This process involves the utilization of deep learning models, complete with synthetic data creation resembling the training set.

## Dependencies

In order to setup and run the GAN Sandbox on your operating system, the following dependencies are to be met:

### Back-End Dependencies

#### Needed to load and run generations (CPU)

* cv2 (OpenCV): A versatile library for computer vision tasks and image processing
* TensorFlow and Keras: Deep learning frameworks for constructing and training neural networks
* numpy: A package for scientific computing with Python
* matplotlib: A plotting library for creating visualizations
* Flask: A lightweight web framework used for constructing the application's back-end

* 64-bit Linux: The project is optimized for 64-bit Linux environments (programmed on Ubuntu distro)
* Python 3.3+: The project supports Python 3.3 and later versions

#### Additional libraries needed for training locally (GPU)

* NVIDIA CUDA: CUDA 8.0+ is recommended for Pascal GPUs
* NVIDIA cuDNN: cuDNN is a GPU-accelerated library for deep neural networks

### Front-End Dependencies
* React: JavaScript Framework for routing and dynamic user interfance
* Material-UI (MUI): A React UI Framework which provides pre-designed template components which are responsive and visually appealing

You can install these dependencies by using 
`npm install`.

## Running The Application
The GAN Sandbox can be executed using `./launch.sh`.

If you are getting permission issues be sure make sure that the file is given execution prems `chmod +x launch.py`.


If you opted to use Miniconda for your installation process of TensorFlow be sure to source the environment before proceeding with the installation process. If you want to use GPU training without Google Colab, refer to the "Additional libraries" under Back-End Dependencies.

## Project Structure

There are five key folders:

* `checkpoints`: Stores our saved model checkpoints for ongoing training process.
* `gen_images`: Contains generated images from the GAN model
* `outputs`: Holds composite images for model validity
* `resized_images`: Includes 32x32 resized images (check section 2.3.1 if you are confused as to why)
* `training`: contains training set <-- PUT YOUR PHOTOS HERE

Please note: **Before Launching** that you have prepared a training set in the `training` folder.

Additional Note: If you circle back to the same output, then all the noise orientations have been used, train for another epoch and generate again.

