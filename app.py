from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
import psycopg2,math,random

app=Flask(__name__)
CORS(app)

load_dotenv()

POSTGRES = {
   'user': os.getenv('PSQL_USER'),
   'pw': os.getenv('PSQL_PWD'),
   'db': os.getenv('PSQL_DB'),
   'host': os.getenv('PSQL_HOST'),
   'port': os.getenv('PSQL_PORT'),
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)
migrate=Migrate(app,db)

class Score(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    wpm=db.Column(db.Float, nullable=False)
    excerpt_id=db.Column(db.Integer, db.ForeignKey('excerpt.id'))

class Excerpt(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    testdata=db.Column(db.String,nullable=False)
    scores=db.relationship('Score', backref='excerpt', lazy=True)
    

@app.route('/excerpts')
def list():
    excerpt=Excerpt.query.all()
    excerptArr=[]
    for e in excerpt:
        excerptArr.append(e.testdata)
    return jsonify(excerptArr)

@app.route('/excerpts/random',methods=['POST','GET'])
def listrandom():
    excerpt=Excerpt.query.all()
    random_num=math.floor(random.random()*len(excerpt))
    score_count=Score.query.filter_by(excerpt_id=excerpt[random_num].id).count()
    top_scores=Score.query.filter_by(excerpt_id=excerpt[random_num].id).all()
    scores=[]
    for score in top_scores:
        scores.append({"score":{"id":score.id,"value":score.wpm}})
    return jsonify({"id":excerpt[random_num].id,"text":excerpt[random_num].testdata,"top_scores":scores,"score_count":score_count})

@app.route('/score', methods=['POST','GET'])
def create():
    if request.method=='POST':
        data=request.get_json()
        print (data)
        score=Score(wpm=data['wpm'],excerpt_id=data['excerpt_id'])
        db.session.add(score)
        db.session.commit()
        return jsonify('success')
    
    return   jsonify("failed")


if __name__ == '__main__': 
    app.run()