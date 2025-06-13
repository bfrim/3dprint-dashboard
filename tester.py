from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <h1>Hello world!</h1>
        <p>I am not a button</p>
        <button>I am a button</button>
    """

if __name__ == '__main__':
    app.run(debug=True)