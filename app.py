from pymatgen import MPRester
from flask import Flask

app = Flask("mat_combiner")



@app.route('/')
def hello():
    return 'Hello!'

