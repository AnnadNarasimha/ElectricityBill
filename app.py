from flask import Flask,render_template,session,url_for
from flask_sqlalchemy import SQLAlchemy
#import admin.py,user.py,worker.py

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

class User(db.Model) :
    uid = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20) , unique = True , nullable = False)
    password = db.Column(db.String(15) , nullable = False)
    phNo = db.Column(db.Integer)
    address = db.Column(db.String(40))

class Worker(db.Model) :
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20) , unique = True , nullable = False)
    password = db.Column(db.String(15) , nullable = False)

class bill(db.Model) :
    id = db.Column(db.Integer , primary_key = True)
    uid = db.Column(db.Integer , nullable = False)
    empId = db.Column(db.Integer , nullable = False)
    amount = db.Column(db.Integer , nullable = False)

@app.route("/" , methods = ['GET' , 'POST'])
def home():
    '''
    if request.method == 'POST' :
        session['username'] = request.form['username']
        password = request.form['password']
        flag = True
        user = db.session.execute("select * from User where username == " + session['username']).first()
        user1 = db.session.execute("select * from Worker where username == " + session['username']).first()
        if user in None and user1 in None :
            return "User not found"
        if user not None :
            if user.password != password :
                return "Invalid password"
            return url_for('userDashboard')
        if user1.username == 'admin' :
            if user1.password == password :
                return url_for('adminDashboard')
            return "Unauthoraised user"
        if user1.password == password :
            return url_for('wrokerDashboard')
        '''
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context() :
        db.create_all()
    app.run(debug=True)