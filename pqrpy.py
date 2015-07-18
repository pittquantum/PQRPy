from urllib2 import Request, urlopen, URLError

class PQRPy(object):

    def __init__(self, key):
        self.key = key

    def json(self):
        request = Request("http://pqr.pitt.edu/api/json/" + self.key)
        try:
            response = urlopen(request)
            json_resp = response.read()
            self.json_resp = json_resp

            return json_resp
        except:
            raise Exception("That key is invalid")

    def mol2(self):
        request = Request("http://pqr.pitt.edu/api/mol/" + self.key)
        try:
            response = urlopen(request)
            mol2_resp = response.read()
            self.mol2_resp = mol2_resp

            return mol2_resp
        except:
            raise Exception("That key is invalid")
