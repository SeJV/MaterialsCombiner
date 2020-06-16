# MaterialsCombiner
Combines Apis of multiple materials databases
Currently included DataBases: 
- Materials Project: from pymatgen import MPRester
- Mendeleev: from mendeleev import element
- OQMD: import qmpy_rester as qr

# Start the service
- python>=3.7
- Install Requirements: `pip install ./requirements.txt`
- Add `.env` File on root directory, with the Key for Materials Project: `MP_KEY=<your_key>`
- Run with `python3 main.py`
