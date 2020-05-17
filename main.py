from flask import Flask
from flask_restful import Resource, Api
from pymatgen import MPRester
import qmpy_rester as qr
from dotenv import load_dotenv
import os
import json
load_dotenv()
MP_KEY = os.getenv("MP_KEY")

app = Flask(__name__)
api = Api(app)


def add_source(obj, source):
    obj["source"] = source
    return obj


class EntriesRequest(Resource):

    def get(self, inp):
        with MPRester(MP_KEY) as m:
            compositions_mp = m.get_data(inp)
            compositions_mp = list(map(lambda comp: add_source(comp, "materials_project"), compositions_mp))

        with qr.QMPYRester() as q:
            compositions_oqmd = q.get_oqmd_phases(verbose=False, composition=inp)["data"]
            compositions_oqmd = list(map(lambda comp: add_source(comp, "oqmd"), compositions_oqmd))

        result = compositions_mp + compositions_oqmd

        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response


api.add_resource(EntriesRequest, '/composition/<string:inp>')
app.run(debug=True)

