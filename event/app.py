#mycursor = mydb.cursor()
#sql = "INSERT INTO data2 (username, password) VALUES (%s, %s)"
#val = ("John", "Highway 21)
#mycursor.execute(sql, val)
#mydb.commit()
#print(mycursor.rowcount, "record inserted.")
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
ANS=["YES","NO","MAYBE"]
list={}

# routing
@app.route("/")
def index():
    return render_template("index.html", ans=ANS)

@app.route("/reg", methods=['POST'])
def reg():

    name=request.form.get("NAME")
    answer=request.form.get("answer")
    list[name]=answer

    return redirect("/data")

@app.route("/data", methods=['GET','POST'])
def data():
    return render_template("data.html", list=list)

# running 
if __name__ == '__main__':
    app.run(debug=True)