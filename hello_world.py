from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World in release branch2!"

if __name__ == "__main__":
    app.run(port=8080)

