from flask import flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.confi['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:Dannya32@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO']= True
db = SQLAlchemy(app)

#create Blogpost Class
class Blogpost (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogtitle = db.Colum(db.String(120))
    blogpost = db.Column(db.String)

    def __init(self, blogtitle,blogpost):
        self.blogtitle = blogtitle
        self.blogpost = blogpost


@app.route('/newpost',methods=['POST','GET'])
def newpost():
    if request.method=='POST':
        blogtitle = request.form['blogtitle']
        blogpost = request.form['blogpost']