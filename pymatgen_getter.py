from pymatgen import MPRester

def get_pymatgen(kwargs):
    with MPRester() as m:
        entries = m.get_data('Al2O3')
