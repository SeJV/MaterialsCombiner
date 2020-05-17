from pymatgen import MPRester
from mendeleev import element
import qmpy_rester as qr
from flask import Flask

app = Flask("mat_combiner")


@app.route('/')
def hello():
    return 'Hello!'

