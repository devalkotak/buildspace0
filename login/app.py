from flask import Flask, render_template, request, redirect
from cs50 import SQL
app=Flask(__name__)
acc={}
db=SQL("sqlite:///login.db") 




@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/reg", methods=['GET','POST'])
def reg():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if db.execute("SELECT 1 FROM accounts WHERE user = ?",username):
            return render_template("error.html",message="USERNAME EXISTS")
        else:
            db.execute("INSERT INTO accounts (user,pass) VALUES(?,?)", username,password)
            acc[username]=password
            return redirect("/")
    else:
        return render_template("error.html",message="GET ERROR")

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
@app.route("/result", methods=['GET','POST'])
def result():
    user1=request.form.get("user1")
    pass1=request.form.get("pass1")
    if db.execute("SELECT 1 FROM accounts WHERE user = ?",user1):
        if db.execute("SELECT * FROM accounts WHERE user = ? AND pass = ?",user1,pass1):
            return render_template("success.html", user=user1, password=pass1)
        return render_template("error.html", message="WRONG PASSWORD")
    else:
        return render_template("error.html", message="WRONG USERNAME")

# running 
if __name__ == '__main__':
    app.run(debug=True)