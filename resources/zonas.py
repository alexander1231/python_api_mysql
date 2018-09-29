from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.zonas import ZonasModel

class Zonas(Resource):
	def get(self, zona):
		zona = ZonasModel.find_by_zona(zona)
		if zona:
			return zona.json()
		return {'message': {'Zonas not found'}}, 404

class ZonasList(Resource):
	def get(self):
		return {'zonas': list(map(lambda x: x.json(), ZonasModel.query.all()))}
