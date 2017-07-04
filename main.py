from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Dannya32@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO']= True
db = SQLAlchemy(app)

#create Blogpost Class
class Blogpost (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogtitle = db.Column(db.String(120))
    blogpost = db.Column(db.String(20000))

    def __init(self, blogtitle,blogpost):
        self.blogtitle = blogtitle
        self.blogpost = blogpost


@app.route('/newpost',methods=['POST','GET'])
def newpost():
    if request.method=='POST':
        blog_title = request.form['blogtitle']
        blog_post = request.form['blogpost']
        new_blog = Blogpost (blog_title,blog_post)

        db.session.add(new_blog)
        db.session.commit()
        return redirect('/blog')

    return render_template('newpost.html')

if __name__ == '__main__':
    app.run()