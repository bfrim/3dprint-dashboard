from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <h1>Hello world!</h1>
        <p>I am not a button</p>
        <a href="{{ url_for('home') }}">Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)