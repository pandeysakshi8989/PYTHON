from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 



@app.route('/show')
def products():
    return 'this is products page'

if __name__ == "__main__":
    app.run(debug=True, port=8000)