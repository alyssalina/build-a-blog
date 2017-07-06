from flask import Flask, request, render_template, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Dannya32@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO']= True
db = SQLAlchemy(app)

app.secret_key = 'K^kzqbF&ZKEY:68fQ=iCY#M&'

#create Blogpost Class
class Blogpost (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogtitle = db.Column(db.String(120))
    blogpost = db.Column(db.String(20000))

    def __init__(self, blogtitle, blogpost):
        self.blogtitle = blogtitle
        self.blogpost = blogpost

@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST','GET'])
def blog():
    blogs = Blogpost.query.all()

    return render_template('blog.html', title="Blogz", blogs=blogs)

@app.route('/newpost',methods=['POST','GET'])
def newpost():
    if request.method=='POST':
        blogtitle = request.form['blogtitle']
        blogpost = request.form['blogpost']
        new_blog = Blogpost(blogtitle, blogpost)

        if blogtitle != "" and blogpost !="":
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blog')
        else:
            flash('Please provide both a blog title and content for your post!','error')

    return render_template('newpost.html')

if __name__ == '__main__':
    app.run()