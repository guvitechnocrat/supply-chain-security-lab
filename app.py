from flask import Flask
import requests  # Potentially vulnerable dependency

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevSecOps!"

if __name__ == "__main__":
    app.run(debug=True)
