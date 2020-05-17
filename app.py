from flask import Flask
from qmpy_getter import get_qmpy_data
from pymatgen_getter import get_pymatgen

app = Flask("mat_combiner")


@app.route('/')
def hello():
    return 'Hello!'

