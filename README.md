# PQRPy


```python
from pqrpy import PQRPy

caller = PQRPy('LOUPRKONTZGTKE-FOEVPDMQSA-N')

# Make the relevant API request once
caller.json()
caller.mol2()

# The object stores the API response for future instant usage
print caller.json_resp
print caller.mol2_resp
```
