from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start-print")
def start_print():
    return render_template("start-print.html")

if __name__ == '__main__':
    app.run(debug=True)