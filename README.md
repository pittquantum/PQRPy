# PQRPy


```python
from pqrpy import PQRPy

key = 'LOUPRKONTZGTKE-FOEVPDMQSA-N'
caller = PQRPy()

molecule_json = caller.json(key)
molecule_mol2 = caller.mol2(key)
```
