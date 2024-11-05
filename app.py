from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def start():
    return "<h1><Mangekant generator</h1><br>"

@app.route("/")
def form():
    pass

if __name__ == '__main__':  
    app.run(debug=True)  
