from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.zonas import Zonas, ZonasList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qa2ws#ED$RF@localhost:3306/Mikrowisp5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'alex'
api = Api(app)

api.add_resource(Zonas, '/zonas/<string:name>')
api.add_resource(ZonasList, '/zonas')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5001, debug=True)
