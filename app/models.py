# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Exam model
class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __repr__(self):
        return '<Exam {}>'.format(self.title)

# Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question_type = db.Column(db.String(50))  # e.g., text, image, code upload
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))

    def __repr__(self):
        return '<Question {}>'.format(self.text)

# Result model
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))

    def __repr__(self):
        return '<Result {}>'.format(self.score)
