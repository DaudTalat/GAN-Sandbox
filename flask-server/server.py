from flask import Flask

app = Flask(__name__)

@app.route("/dauds")
def dauds():
    print("oh wow")
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)