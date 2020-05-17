import qmpy_rester as qr
import json


def get_qmpy_data(kwargs):
    with qr.QMPYRester() as q:
        list_of_data = q.get_oqmd_phases(**kwargs)

        if list_of_data["data"]:
            with open('oqmd.json', 'w') as fp:
                json.dump(list_of_data['data'], fp, indent=4)




