#mycursor = mydb.cursor()
#sql = "INSERT INTO data2 (username, password) VALUES (%s, %s)"
#val = ("John", "Highway 21)
#mycursor.execute(sql, val)
#mydb.commit()
#print(mycursor.rowcount, "record inserted.")
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
list=[]

# routing
@app.route("/")
def index():
    return render_template("index.html", list=list)

@app.route("/reg", methods=['POST'])
def reg():

    name=request.form.get("task")
    list.append(name)
    return redirect("/")

@app.route("/rem", methods=['POST'])
def rem():

    list.pop()
    return redirect("/")


# running 
if __name__ == '__main__':
    app.run(debug=True)