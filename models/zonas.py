import sqlite3
from db import db

class ZonasModel(db.Model):
	__tablename__ = 'zonas'

	id = db.Column(db.Integer, primary_key=True)
	zona = db.Column(db.String(47))

	def __init__(self, zona):
		self.zona = zona

	def json(self):
		return {'zona': self.zona}

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_zona(cls, zona):
		return cls.query.filter_by(zona=zona).first()

	@classmethod
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

