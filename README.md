# GAN-Sandbox

The GAN Sandbox environment is a interactive web-application configured to allow users to generate artistic images using the power of Generative Adversarial Networks (GANs). This process involves the utilization of deep learning models, complete with synthetic data creation resembling the training set.

## Dependencies

In order to setup and run the GAN Sandbox on your operating system, the following dependencies are to be met:

### Back-End Dependencies

#### Needed to load and run generations (CPU)

* cv2 (OpenCV): A versatile library for computer vision tasks and image processing
* TensorFlow and Keras: Crucial deep learning frameworks for constructing and training neural networks
* numpy: A fundamental package for scientific computing with Python.
matplotlib: A comprehensive plotting library for crafting visualizations.
* Flask: A lightweight web framework used for constructing the application's back-end

* 64-bit Linux: The project is optimized for 64-bit Linux environments.
Python 2.7 or 3.3+: The project supports both Python 2.7 and Python 3.3 and later versions

#### Additional libraries needed for training locally (GPU)

* NVIDIA CUDA 7.5 or 8.0: CUDA 7.5 is required, but CUDA 8.0 is recommended for Pascal GPUs
* NVIDIA cuDNN v4.0 or v5.1: cuDNN is a GPU-accelerated library for deep neural networks. The project requires at least version 4.0, but version 5.1 is recommended

### Front-End Dependencies
* React: JavaScript Framework for routing and dynamic user interfance. 
* Material-UI (MUI): A React UI Framework which provides pre-designed template components which are responsive and visually appealing

You can install these dependencies by using 
`npm install`.

## Running The Application
The GAN Sandbox can be executed using `./launch.sh`

If you are getting permission issues be sure make sure that the file is given execution prems `chmod +x launch.py`


If you opted to use Miniconda for your installation process of TensorFlow be sure to source the environment before proceeding with the installation process. If you want to use GPU training without Google Colab, refer to the "Additional libraries" under Back-End Dependencies.
