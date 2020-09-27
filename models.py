from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Flight(db.Model):
    #flight isimli bir table oluştur
    __tablename__ = "flights"
    #table'ın içine column'lar ekle
    id = db.Column(db.Integer, primary_key = True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
    __tablename__ ="passengers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Integer, primary_key=True)
    #flights table'ından id kısmını referans aldırıyoruz foreignkey kullanarak
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

#its workin that way