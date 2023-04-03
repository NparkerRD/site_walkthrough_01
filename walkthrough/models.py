from flask import Flask
from walkthrough import db

class Company(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    locations = db.relationship('Location', backref="location_company")

    def create_company(self):
        pass

    def delete_company(self):
        pass


class Location(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=50), nullable=False)
    company_id = db.Column(db.Integer(), db.ForeignKey('company.id'))
    sites = db.relationship('Site', backref="site_location")

    def create_location():
        pass
    
    def delete_location():
        pass

class Site(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    location_id = db.Column(db.Integer(), db.ForeignKey('location.id'))