# MaterialsCombiner
Combines Apis of multiple materials databases
Currently included DataBases: 
- Materials Project: from pymatgen import MPRester
- Mendeleev: from mendeleev import element
- OQMD: import qmpy_rester as qr

##  Start the service
- python>=3.7
- Install Requirements: `pip install ./requirements.txt`
- Add `.env` File on root directory, with the Key for Materials Project: `MP_KEY=<your_key>`
- Run with `python3 main.py`

## Use the service
- on `port:5000` ist the service now available
- get information with a `GET request` on path `/formula/<your_input>`
  - Information gets cached locally, so the next time you reqest the same data, it will be much faster
  - Additionally you can use: '-' for OR, ',' for AND, e.g. (Fe-Mn),O for the OQMD database
  
  
## Adding databases
- Additional databases with API
  - With Flask requests, any available API that has a formula as Input and returns an json object is addable
  - In the `main.py` inside the `get` function, there is an `inp` parameter, that represents the formula as string
  - This can be used to fetch a request, and results of such a request should be added to the `data_in_json` object 
- Additional databases with python package
  - Similar to API approach, you can add databases that are available as python packages, such as
    - AFLOW: https://pypi.org/project/aflow/
    - Citrination: https://citrineinformatics.github.io/python-citrination-client/index.html
    - COD: https://pypi.org/project/crystals/
    - ICSD: https://github.com/hegdevinayi/icsd-queryer
  - Those are easier to implement, because you don't need an additional Flask app, but can use the already implemented functions
  - If the response format from the api is not available in json, you need to transform it to json
  - Concatenate the results into the `data_in_json` object in the `main.py` file inside the get function, with the key as the identifier for the database
