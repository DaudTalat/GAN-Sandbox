import os

from flask import Flask, jsonify
from flask import send_file
from GAN import GAN
import sys
import multiprocessing

app = Flask(__name__)
process_thread = None

checkpoint_name = ""
resolution = "SR"


# Helper Function
# Creates and trains model
def start_training():

    gen_model = descrim_model = GAN_model = None

    if resolution == "SR":
        try:
            print("Training on SR.")
            gen_model, descrim_model, GAN_model =  GAN.export_models_128(checkpoint_name)
        except:
            print("Error: Be sure to use HQ model when training HQ images.")
            gen_model, descrim_model, GAN_model = GAN.export_models(checkpoint_name)

    elif resolution == "HR":
        try:
            print("Training on HR.")
            gen_model, descrim_model, GAN_model =  GAN.export_models(checkpoint_name)
        except:
            print("Error: Be sure to use SR model when training SR images.")
            gen_model, descrim_model, GAN_model = GAN.export_models_128(checkpoint_name)

    GAN.train(gen_model, descrim_model, GAN_model, 29000, 16, 100, 250, 10)

# Trains Generative Image AI
# Note: We are using multi-processing instead of threads to release the lock
@app.route("/train")
def train():
    print("Starting Training...")

    try:
        global process_thread

        if process_thread is None or not process_thread.is_alive():
            process_thread = multiprocessing.Process(target=start_training)
            process_thread.start()
            return jsonify(message="Training Started...")
        else:
            process_thread.terminate()
            process_thread.join()
            process_thread = None
            return jsonify(message="Training Stopped.")
    except:
        print("Make sure you entered the checkpoint name correctly.")

# Uses the Checkpoint to Generate Images
# Model is labeled as "SR - Standard Resolution" or "HR - High Resolution"
# Otherwise we do not know what ckpt model we are using until we hit an error. 
@app.route("/generate")
def generate():
    print("Generating Images...")

    if process_thread is None or not process_thread.is_alive():
        process_thread = multiprocessing.Process(target=start_training)
        process_thread.start()
    
    try:
        if resolution == "SR":
            try:
                print("Training on SR.")
                gen_model, _, _ =  GAN.export_models_128(checkpoint_name)
            except:
                print("Error: Be sure to use HQ model when training HQ images.")
                gen_model, _, _ = GAN.export_models(checkpoint_name)

        elif resolution == "HR":
            try:
                print("Training on HR.")
                gen_model, _, _ =  GAN.export_models(checkpoint_name)
            except:
                print("Error: Be sure to use SR model when training SR images.")
                gen_model, _, _ = GAN.export_models_128(checkpoint_name)

        GAN.save_images(gen_model)

    except:
        print("Make sure you entered the checkpoint name correctly.")
    
    return jsonify("Generation Completed.")

# Get Image Complement (e.g. 0 -> newest photo, 1 -> second newest image)
@app.route("/gen_images/<int:id>")
def get_photo(id):
    num_elements = len(os.listdir(os.getcwd() + "/flask-server/GAN/gen_images"))
    return send_file(os.getcwd() + "/flask-server/GAN/gen_images/{}.png".format(num_elements - id), mimetype="image/gif")

@app.route("/ckpt/<string:name>")
def set_ckpt(name):
    global checkpoint_name 
    checkpoint_name = name
    print("Checkpoint is " + name)
    return jsonify("Model Checkpoint {} Set!".format(name))


@app.route("/setres/<string:res>")
def set_res(res):
    global resolution
    resolution = res
    print("Resolution is " + res)
    return jsonify("Resolution {} Set!".format(res))

if __name__ == "__main__":
    app.run(debug=True)
