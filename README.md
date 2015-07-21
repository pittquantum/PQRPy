# PQRPy


```python
from pqrpy import PQRPy

key = 'LOUPRKONTZGTKE-FOEVPDMQSA-N'
caller = PQRPy(key)

molecule_json = caller.json() # Returns a JSON string
molecules_json_dict = caller.json_dict() # Returns a dictionary with molecular data
molecule_mol2 = caller.mol2() # Returns a MOL2 file as a string

weekly_molecules = caller.weekly() # Returns a list formatted like
                                   # [(InchiKey, Name), (InchiKey, Name), ...]

inchikeys = caller.inchikeys() # Returns a list of InChIKeys
```
