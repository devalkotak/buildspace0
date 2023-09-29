#initialising

from flask import Flask, render_template, request

app=Flask(__name__)

def searchtext(text):
    if (text=="flask"):
        return "FLASK SEARCH"
    else:
        return "TRY SOMETHING ELSE"

# running 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=['GET','POST'])
def search():
    text=request.form['text']
    response=searchtext(text)

    return render_template("index.html",response=response)

if __name__ == '__main__':
    app.run(debug=True)