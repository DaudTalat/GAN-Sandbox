from flask import Flask, jsonify
from GAN import GAN
import sys
import multiprocessing

app = Flask(__name__)
process_thread = None

# Helper Function
# Creates and trains model
def start_training():
    gen_model, descrim_model, GAN_model =  GAN.export_models()
    GAN.train(gen_model, descrim_model, GAN_model, 29000, 32, 100, 250, 100)

# Trains Generative Image AI
# Note: We are using multi-processing instead of threads to release the lock
@app.route("/train")
def train():
    global process_thread

    if process_thread is None or not process_thread.is_alive():
        process_thread = multiprocessing.Process(target=start_training)
        process_thread.start()
        return jsonify(message="Training Started...")
    else:
        process_thread.terminate()
        process_thread.join()
        process_thread = None
        return jsonify(message="Training Finished.")

# Uses the Checkpoint to Generate Images
@app.route("/generate")
def generate():
    print("Generating Images...")

    gen_model, _, _ =  GAN.export_models()
    GAN.save_images(gen_model)

    return jsonify("Generation Completed.")

# Test Route
@app.route("/test")
def stop():
    return jsonify("Hello World!")

if __name__ == "__main__":
    app.run(debug=True)
