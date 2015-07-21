from urllib2 import Request, urlopen, URLError

class PQRPy(object):

    def __init__(self, key):
        self.key = key
        self.json_str = None
        self.mol2_str = None

    def json(self):
        """Make a JSON API call to PQR

        Returns a JSON string containing the data for that molecule
        """

        request = Request("http://pqr.pitt.edu/api/json/" + self.key)
        try:
            response = urlopen(request)
            read_json = response.read()
            self.json_str = read_json
            return read_json
        except:
            raise Exception("That key is invalid")

    def json_dict(self):
        import json

        if not self.json_str:
            self.json_str = self.json()
        return json.loads(self.json_str)

    def mol2(self, key):
        """Make a MOL2 API call to PQR

        Keyword arguments:
        key -- the InChIKey for the molecule

        Returns a string containing the MOL2 data for that molecule
        """

        request = Request("http://pqr.pitt.edu/api/mol/" + key)
        try:
            response = urlopen(request)
            read_mol2 = response.read()
            self.mol2_str = read_mol2
            return read_mol2
        except:
            raise Exception("That key is invalid")

    def weekly(self):
        """Make a API call to PQR to get the molecules of the week

        Returns a list of tuples, each tuple being (InChIKey, Name)
        """

        request = Request("http://pqr.pitt.edu/api/weekly/")
        try:
            response = urlopen(request)
            mol_list = response.read().split("\n")
            weekly = [tuple(x.split(",")) for x in mol_list] 

            return weekly
        except URLError:
            raise Exception("Something went wrong")

    def inchikeys(self):
        """Make a API call to PQR to get all the InChIKeys PQR indexes

        Returns a list containing InChIKeys
        """

        request = Request("http://pqr.pitt.edu/api/inchikeys")
        try:
            response = urlopen(request)
            read_inchi = response.read().split("\n")

            return read_inchi
        except:
            raise Exception("Something went wrong")
