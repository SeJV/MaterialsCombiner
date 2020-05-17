from pymatgen import MPRester
from mendeleev import element
from flask import Flask

app = Flask("mat_combiner")


@app.route('/')
def hello():
    return 'Hello!'

