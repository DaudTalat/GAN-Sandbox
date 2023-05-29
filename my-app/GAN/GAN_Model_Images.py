# Written By Daud Talat

# GENERATOR MODEL INFO:
# Model: "sequential"

# Import Modules
import os
import cv2 as cv # Image processing (COMP VISION LIB)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Remove Cluttering for Debug
#from tensorflow.python.keras.optimizer_v2.adam import Adam
from tensorflow.python.keras.layers import LeakyReLU
from keras.layers import Dropout # For regularization
from keras.layers import Reshape
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import Conv2DTranspose
from keras.models import Sequential 
from keras.optimizers import Adam
from keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt

saved_image_id = 0 # Need to store this as a static to assign IDs

def main():
    gen, descrim, GAN = export_models()

# The train function is responsible for training the 
def train(generator : Sequential, discriminator: Sequential, GAN : Sequential, epoch, batch=32, output_interval=250, latent_space_dim=100): 
    # Use Cifar Dataset for priminary training
    (training_images, _), (_, _) =  cifar10.load_data()

    # Calculate batches for each epoch
    epoch_batch_size = int(training_images[0] // batch) # Note that we care about 0 dim since each column represents a feature value, not row.

    real_lables = np.ones((batch), 1)
    generated_lables = np.ones((batch, 1))

    for epo in range(epoch):
        for i in range(epoch_batch_size):

            # Descriminator loss refers to real image loss
            # GAN loss refers to how well generator can fool descriminator

            # We need to pass generative noise as our latent space to make random predictions
            gen_noise = np.random.normal(0, 1, (batch, latent_space_dim))
            gen_images = generator.predict(gen_noise)

            # We need batch indices for the size allotted
            batch_indices = np.random.choice(training_images.shape[0], size=batch, replace=False) ## --> DEV NOTE: THIS LINE MIGHT CAUSE A BUG ##
            batch_images = training_images[batch_indices]

            # Train
            discrimator_loss = 0.5 * np.add(discriminator.train_on_batch(batch_images, real_lables), discriminator.train_on_batch(gen_images, generated_lables))

            gan_noise = np.random.normal(0, 1, (batch, latent_space_dim))
            gan_loss = GAN.train_on_batch(gan_noise, real_lables) # now we test performance 

            print("This is epoch {}, the descriminator loss is {}, and the GAN loss is {}".format(epo, discrimator_loss, gan_loss))
        
            if epo % output_interval == 0:
                save_images(generator)

# This function will be used to generate a new image for each output interval in the training step
def save_images(generator : Sequential):
    global saved_image_id

    print(saved_image_id)

    random_vectors = np.random.normal(0, 1, (4 * 4, 100)) # Rows * Cols = Batch_Size, 100 Latent Space Dim

    # Use random latent space vectors to "predict" images
    gen_model_imgs = generator.predict(random_vectors)

    saved_image_id += 1

    gen_model_imgs = (gen_model_imgs + 1) * 0.5
    
    counter = 0 
    # Matplot used to make grid of subplots for generated image (e.g. 4x4 in our case)
    figure, axis = plt.subplots(4, 4)

    for i in range(4):
        for j in range(4):
            axis[i, j].imshow(gen_model_imgs[counter])
            axis[i, j].axis('off') # Just want images, no axis nums
            counter += 1 # next image (on 4x4 grid)
            
    figure.savefig("my-app/GAN/outputs/%s.png" % saved_image_id)

def export_models():

    # Adjust these values for higher or lower quality of image
    img_x_dim = 128
    img_y_dim = 128

    img_dims = (img_x_dim, img_y_dim) # Image resolution

    # Relative Paths
    img_path = os.path.join(os.getcwd(), "my-app/GAN/training/")
    resized_img_dir = os.path.join(os.getcwd(), "my-app/GAN/resized_images/") # make sure images are sized to 64x64

    index = 0
    # Lets ignore any none image files (or non-supported image files)
    for img in os.listdir(img_path):
        if not img.endswith((".jpg", ".png", ".jpeg")):
            continue    
        
        resized_img = cv.imread(os.path.join(img_path, img))
        resized_img = cv.resize(resized_img, img_dims) 

        cv.imwrite(resized_img_dir + "{}.png".format(index), resized_img) 

        index += 1

    # Optmizer and Encoding Latent Space
    img_shape = (img_x_dim, img_y_dim, 3) # 64x64 image with RGB
    latent_space_dim = 100 # encoding of features dimensionality

    # Create Generator (since we are using 128 we need to use 128/2^n where n is represented by the number of hidden layers (i.e. 128/2^3 = 16) 
    gen_model = Sequential()

    # The add() function adds layers to model

    # Input Layer (dense) In 
    gen_model.add(Dense(units = 256 * 16 * 16, input_shape=(latent_space_dim, )))
    gen_model.add(LeakyReLU(alpha=0.2)) # This adds leaky relu as activation func for NN layer (should be all the same for the case of our image model)
    gen_model.add(Reshape((16,16,256))) # Needed as we switch to convolutional layers, to bridge gap (Dense -> Conv / 1D -> 4D)

    # Hidden Layers (conv2Dtrans)
    # image upsampling layer | 128 filters which are 4x4 | stride of (2,2) to increase detail (smaller steps) | padding to perserve input image
    # Input space increases by 2x 
    gen_model.add(Conv2DTranspose(filters=128, kernel_size=(4,4), strides=(2,2), padding="same"))  
    gen_model.add(LeakyReLU(alpha=0.2))

    gen_model.add(Conv2DTranspose(filters=128, kernel_size=(4,4), strides=(2,2), padding="same"))  
    gen_model.add(LeakyReLU(alpha=0.2))

    gen_model.add(Conv2DTranspose(filters=128, kernel_size=(4,4), strides=(2,2), padding="same"))  
    gen_model.add(LeakyReLU(alpha=0.2))

    # Output Layer (conv2D)
    gen_model.add(Conv2D(filters=3, kernel_size=(4,4), activation="tanh", padding="same"))

    # Create Descriminator
    descrim_model = Sequential()

    # Input Layer (Generated Image)
    descrim_model.add(Conv2D(filters=64, kernel_size=(4,4), padding="same", input_shape=img_shape))
    descrim_model.add(LeakyReLU(alpha=0.2))

    # Hidden Layer (Extract Features)
    descrim_model.add(Conv2D(filters=128, kernel_size=(4,4), padding="same"))
    descrim_model.add(LeakyReLU(alpha=0.2))

    descrim_model.add(Conv2D(filters=128, kernel_size=(4,4), padding="same"))
    descrim_model.add(LeakyReLU(alpha=0.2))

    descrim_model.add(Conv2D(filters=128, kernel_size=(4,4), padding="same"))
    descrim_model.add(LeakyReLU(alpha=0.2))

    # Output (Flatten)
    descrim_model.add(Flatten())
    descrim_model.add(Dropout(0.4))
    descrim_model.add(Dense(units=1, activation="sigmoid"))


    # COMPILE
    descrim_model.compile(loss="binary_crossentropy", optimizer=Adam(learning_rate=0.0002), metrics=["accuracy"])

    # Make GAN
    GAN_model = Sequential()
    descrim_model.trainable = False # We don't want to train descriminator while training GAN

    # Assemble 
    GAN_model.add(gen_model)
    GAN_model.add(descrim_model)

    GAN_model.compile(loss="binary_crossentropy", optimizer=Adam(learning_rate=0.0002), metrics=["accuracy"])

    print("Models Exported")
    return gen_model, descrim_model, GAN_model

if __name__ == '__main__':
    main()