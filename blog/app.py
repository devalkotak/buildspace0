#initialising

from flask import Flask, render_template, request

app=Flask(__name__)

# routing

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/links")
def links():
    return render_template("links.html", name=request.args.get("name", "!!!!!!!!!"))
@app.route("/resources")
def resources():
    return render_template("resources.html",name=request.args.get("name", "!!!!!!!!!"))

# running 
if __name__ == '__main__':
    app.run(debug=True)