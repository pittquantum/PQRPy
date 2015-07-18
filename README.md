# PQRPy


```python
from pqrpy import PQRPy

key = 'LOUPRKONTZGTKE-FOEVPDMQSA-N'
caller = PQRPy()

molecule_json = caller.json(key) # Returns a JSON string
molecule_mol2 = caller.mol2(key) # Returns a MOL2 file as a string

weekly_molecules = caller.weekly() # Returns a list formatted like
                                   # [(InchiKey, Name), (InchiKey, Name), ...]
```
