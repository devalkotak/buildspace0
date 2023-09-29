#initialising

from flask import Flask, render_template, request

app=Flask(__name__)

# counting
def countword(text):
    word=text.split()
    return len(word)

def countpara(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

def countchar(text):
    text=text.replace('\n','')
    text=text.replace('\r','')
    return len(text)

# routing

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count",methods=['GET','POST'])
def count():
    text =request.form['text']
    words=countword(text)
    paras=countpara(text)
    chars=countchar(text)

    return render_template("index.html",words=words,paras=paras,chars=chars)

# running 

if __name__ == '__main__':
    app.run(debug=True)