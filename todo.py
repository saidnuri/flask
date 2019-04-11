from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Said/PycharmProjects/flask_den/todo.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    return render_template("index.html")
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    complate=db.Column(db.Boolean)
if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
