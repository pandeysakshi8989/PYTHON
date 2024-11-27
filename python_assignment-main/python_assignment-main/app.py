from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
import datetime

def utcnow():
    return datetime.datetime.utcnow()


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=utcnow)

with app.app_context():
    db.create_all()


#Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
    return render_template('index.html') 

#about page
@app.route('/about')
def about():
    return render_template('about.html') 
#show page
@app.route('/show')
def products():
    return 'this is products page'

#main method
if __name__ == "__main__":
    app.run(debug=True, port=8000)