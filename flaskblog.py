from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<H1>Home Page!</H1>"

@app.route("/about")
def about():
    return "<H1>About Page!</H1>"

if __name__ == '__main__':
    app.run(debug=True)