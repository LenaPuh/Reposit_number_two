from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consultant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    work_days = db.Column(db.String(20), default='1,2,3,4,5')
    appointments = db.relationship('Appointment', backref='consultant')