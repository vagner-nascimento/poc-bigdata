from flask import jsonify, request
from flask_restful import Resource

class TaxRoutes(Resource):
    # get the total taxes for the month over the amount
    def get(self):
        year = int(request.args.get("year"))
        month = int(request.args.get("month"))
        amount = int(request.args.get("amount"))
        amount = amount / 100
        year = year / 100
        
        tax = 0        
        if(month % 2 == 0):
            tax = (amount * 0.05) + year
        else:
            tax = (amount * 0.02) + year

        tax = tax * 100
        
        return jsonify({ "totalTaxes": int(tax) })
