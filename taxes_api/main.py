from flask import Flask
from flask_restful import Api
from tax_routes import TaxRoutes

app = Flask(__name__)
api = Api(app)

api.add_resource(TaxRoutes, "/tax")

if __name__ == "__main__":
    app.run(port=80, debug=True)
