from urllib2 import Request, urlopen, URLError

class PQRPy(object):

    def __init__(self):
        pass

    def json(self, key):
        request = Request("http://pqr.pitt.edu/api/json/" + key)
        try:
            response = urlopen(request)
            read_json = response.read()
            return read_json
        except:
            raise Exception("That key is invalid")

    def mol2(self, key):
        request = Request("http://pqr.pitt.edu/api/mol/" + key)
        try:
            response = urlopen(request)
            read_mol = response.read()
            return read_mol
        except:
            raise Exception("That key is invalid")
