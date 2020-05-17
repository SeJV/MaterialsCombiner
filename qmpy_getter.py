import qmpy_rester as qr


def get_qmpy_data(kwargs):
    with qr.QMPYRester() as q:
        list_of_data = q.get_oqmd_phases(**kwargs)

        if list_of_data["data"]:
            return list_of_data['data']




