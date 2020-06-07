from flask import Flask
from flask_restful import Resource, Api
from pymatgen import MPRester
import qmpy_rester as qr
import simplejson as json
from parser import parse_formula
from mendeleev import get_table
from cache import Cache

app = Flask(__name__)
api = Api(app)
table = get_table("elements")

class EntiriesRequest(Resource):
    def __init__(self):
        """cache for 1 day"""
        self._cache = Cache("requests.db", 86400)

    def get(self, inp):
        cached_response = self._cache.getResponse("/formula/" + inp)

        if cached_response is not None:
            data_in_json = cached_response
        else:
            with MPRester("uJkhmuvzyyMdO5qHZX") as m:
                mp_data = m.get_data(inp)

            with qr.QMPYRester() as q:
                qr_data = q.get_oqmd_phases(verbose=False, composition=inp)


            elements = [*parse_formula(inp)]
            elements_data = [(table[table['symbol'] == e]).to_dict() for e in elements]

            data_in_json = json.dumps({
                    'mp': mp_data,
                    'qr': qr_data,
                    'elements': elements_data
            }, ignore_nan=True)

        self._cache.saveResponse("/formula/" + inp, data_in_json)

        response = app.response_class(
            response=data_in_json,
            status=200,
            mimetype='application/json'
        )
        return response

api.add_resource(EntiriesRequest, '/formula/<string:inp>')

app.run(debug=True)