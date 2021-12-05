class User:

    def __init__(self, _id=None, fName=None, lName=None):
        self.id = _id
        self.fName = fName
        self.lName = lName

    def __str__(self):
        return f"{self.id}: {self.fName} {self.lName}"

    def create_from_dict(self, data):
        self.id = data['id']
        self.fName = data['fName']
        self.lName = data['lName']