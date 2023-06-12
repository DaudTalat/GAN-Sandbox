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
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


saved_image_id = 0 # Need to store this as a static to assign IDs

def export_models(checkpoint_path=""):
    # Adjust these values for higher or lower quality of image
    img_x_dim = 128
    img_y_dim = 128

    img_dims = (img_x_dim, img_y_dim) # Image resolution

    # Relative Paths

    print(os.path.join(os.getcwd(), "flask-server/GAN/training/"))
    img_path = os.path.join(os.getcwd(), "flask-server/GAN/training/")
    resized_img_dir = os.path.join(os.getcwd(), "flask-server/GAN/resized_images/") # make sure images are sized to 64x64

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
    discrim_model = Sequential()

    # Input Layer (Generated Image)
    discrim_model.add(Conv2D(filters=64, kernel_size=(4,4), padding="same", input_shape=img_shape))
    discrim_model.add(LeakyReLU(alpha=0.2))

    # Hidden Layer (Extract Features)
    discrim_model.add(Conv2D(filters=128, kernel_size=(4,4), padding="same"))
    discrim_model.add(LeakyReLU(alpha=0.2))

    discrim_model.add(Conv2D(filters=128, kernel_size=(4,4), padding="same"))
    discrim_model.add(LeakyReLU(alpha=0.2))

    discrim_model.add(Conv2D(filters=256, kernel_size=(4,4), padding="same"))
    discrim_model.add(LeakyReLU(alpha=0.2))

    # Output (Flatten)
    discrim_model.add(Flatten())
    discrim_model.add(Dropout(0.4))
    discrim_model.add(Dense(units=1, activation="sigmoid"))

    # COMPILE
    discrim_model.compile(loss="binary_crossentropy", optimizer=Adam(learning_rate=0.0002), metrics=["accuracy"])

    # Make GAN
    GAN_model = Sequential()
    discrim_model.trainable = False # We don't want to train descriminator while training GAN

    # Assemble 
    GAN_model.add(gen_model)
    GAN_model.add(discrim_model)

    GAN_model.compile(loss="binary_crossentropy", optimizer=Adam(learning_rate=0.0002), metrics=["accuracy"])

    print("Models Exported")

    load_checkpoint(gen_model, discrim_model, GAN_model, checkpoint_path)

    # Debug
    # print(gen_model.summary())
    # print(discrim_model.summary())
    return gen_model, discrim_model, GAN_model

# This function will be used to load in our weights so that we can save model over severall runs (i.e. checkpoint our progress)
# 1. Checkpoint name specified os.path.join(os.getcwd() + "/flask-server/GAN/checkpoints", "EdwardHopper.h5")
# 2. There is no checkpoints (produce new)
# 3. Use highest increment of checkpoint
def load_checkpoint(generator: Sequential, discriminator: Sequential, GAN: Sequential, checkpoint_path=""):
    global epo_ck_max

    if checkpoint_path == "": # If this is not triggered we are using a specific ck (e.g. EdwardHopper.h5)

        greatest = -1

        for ck in os.listdir(os.getcwd() + "/flask-server/GAN/checkpoints"):

            ck_num = int(ck.split("_")[1].strip(".h5"))
            if ck_num > greatest:
                greatest = ck_num

        if greatest == -1:
            return # Produce new ck (there are none)
        
        else:
            checkpoint_path = os.getcwd() + "/flask-server/GAN/checkpoints/checkpoint_{}.h5".format(greatest) # Use highest increment of ck
            epo_ck_max = greatest

    else: 
        checkpoint_path = os.getcwd() + "/flask-server/GAN/checkpoints/{}".format(checkpoint_path) # Use highest increment of ck
    
    GAN.load_weights(checkpoint_path)
    generator.set_weights(GAN.layers[0].get_weights())
    discriminator.set_weights(GAN.layers[1].get_weights())

# The train function is responsible for training the 
def train(generator : Sequential, discriminator: Sequential, GAN : Sequential, epoch, batch=32, latent_space_dim=100, output_interval=250, checkpoint_interval=1000): 
    
    checkpoint_dir = os.path.join(os.getcwd(), "flask-server/GAN/checkpoints/")

    real_lables = np.ones((batch, 1))
    generated_lables = np.zeros((batch, 1))

    resized_img_dir = os.path.join(os.getcwd(), "flask-server/GAN/resized_images/") # make sure images are sized to 64x64

    training_images = []

    # Encode our img files with NumPy
    for img_file in os.listdir(resized_img_dir):
        img_path = os.path.join(resized_img_dir, img_file)
        img = cv.imread(img_path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        training_images.append(np.asarray(img))
        
    training_images = np.array(training_images)

    # This is a normalization technique needed for convolution (praise COMP4102!!!) [-1, 1] better convergence
    training_images = (training_images - 127.5) / 127.5

    # Calculate batches for each epoch
    epoch_batch_size = int(training_images.shape[0] / batch) # Note that we care about 0 dim since each column represents a feature value, not row.

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
            discrimator_loss_real = discriminator.train_on_batch(batch_images, real_lables)
            discriminator_loss_gen = discriminator.train_on_batch(gen_images, generated_lables)

            gan_noise = np.random.normal(0, 1, (batch, latent_space_dim))

            gan_loss = GAN.train_on_batch(gan_noise, real_lables) # now we test performance 

            print("This is epoch {}, the descriminator loss is {}, and the GAN loss is {}".format(epo, discrimator_loss_real, gan_loss))

        # 9 photos grid
        if epo % output_interval == 0:
            save_images(generator)

        # checkpoint
        if epo % checkpoint_interval == 0:
            checkpoint_path = os.path.join(checkpoint_dir, "checkpoint_{}.h5".format(epo + epo_ck_max))
            GAN.save_weights(checkpoint_path)
            print("Checkpoint Saved at epoch {}".format(epo))

# This function will be used to generate a new image for each output interval in the training step
def save_images(generator : Sequential):

    random_vectors = np.random.normal(0, 1, (4 * 4, 100)) # Rows * Cols = Batch_Size, 100 Latent Space Dim

    # Use random latent space vectors to "predict" images
    gen_model_imgs = generator.predict(random_vectors)
    gen_model_imgs = (gen_model_imgs + 1) * 0.5 # Rescale images [-1,1] -> [0,1]

    # Get max for generated images
    greatest = 0

    for output in os.listdir(os.getcwd() + "/flask-server/GAN/gen_images"):
        output_num = int(output.split(".")[0])
        if output_num > greatest:
            greatest = output_num

    # Save Images (1 .. 5)
    for i in range(5):
        plt.imsave(os.getcwd() + "/flask-server/GAN/gen_images/{}.png".format(greatest + i + 1), gen_model_imgs[i])

    # Get max for generation images
    greatest = 0

    for output in os.listdir(os.getcwd() + "/flask-server/GAN/outputs"):
        output_num = int(output.split(".")[0])
        if output_num > greatest:
            greatest = output_num
 
    counter = 0 
    # Matplot used to make grid of subplots for generated image (e.g. 4x4 in our case)
    figure, axis = plt.subplots(4, 4)

    for i in range(4):
        for j in range(4):
            axis[i, j].imshow(gen_model_imgs[counter])
            axis[i, j].axis('off') # Just want images, no axis nums
            counter += 1 # next image (on 4x4 grid)
            
    # Save Generation
    figure.savefig("flask-server/GAN/outputs/{}.png".format(greatest + 1))

    # gen_model_imgs[0].savefig("flask-server/GAN/gen_images/{}.png".format("0"))
