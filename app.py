from qmpy_getter import get_qmpy_data
from flask import Flask

app = Flask("mat_combiner")



@app.route('/')
def hello():
    return 'Hello!'

