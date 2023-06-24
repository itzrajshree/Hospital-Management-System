from flask import Flask,render_template,request 
from flask_mysqldb import MySQL
import os

PEOPLE_FOLDER=os.path.join('static','folder') 
app=Flask( name  )

app.config['MYSQL_HOST']='localhost' 
app.config['MYSQL_USER']='root' 
app.config['MYSQL_PASSWORD']='********************' 
app.config['MYSQL_DB']='hospital'
mysql = MySQL(app) 
app.config['UPLOAD_FOLDER']=PEOPLE_FOLDER
@app.route('/')


def homepage(): 
    full_filename=os.path.join(app.config['UPLOAD_FOLDER'],'Hope.jpg') 
    return render_template("Homepage.html",user_image= full_filename)
@app.route('/appointment',methods=['GET','POST']) 
def appointment():
    full_filename=os.path.join(app.config['UPLOAD_FOLDER'],'Hope.jpg') 
    if request.method=="POST":
        details=request.form 
        firstname=details['fname'] 
        lastname=details['lname'] 
        age=details['fage'] 
        problem=details['fproblem'] 
        physician=details['fphysician'] 
        phno=details['fmobile'] 
        timings=details['ftime'] 
        cur=mysql.connection.cursor()
    cur.execute("INSERT INTO form(firstname,lastname,age,problem,physician,phno,tim ings) VALUES (%s,%s,%s,%s,%s,%s,%s)",(firstname,lastname,age,problem,physician,phno,timings))
    mysql.connection.commit() 
    cur.close()
    return render_template('display.html',user_image= full_filename) 
    return render_template("Appointment.html",user_image= full_filename)

@app.route('/aboutus',methods=['GET'])
def aboutus(): 
    full_filename=os.path.join(app.config['UPLOAD_FOLDER'],'Hope.jpg') 
    return render_template("about us.html",user_image= full_filename)

if name ==" main ": app.run()
