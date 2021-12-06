from card_representation import CardRepresentation
class User:

    def __init__(self, _id=None, fName=None, lName=None, user_name=None, password=None):
        self.id = _id
        self.fName = fName
        self.lName = lName
        self.user_name = user_name
        self.password = password
        self.cardsInfo: list(CardRepresentation) = []

    def __str__(self):
        return f"{self.id}: {self.fName} {self.lName} -- {self.user_name}, {self.password}"

    def create_from_dict(self, data):
        self.id = data['id']
        self.fName = data['fName']
        self.lName = data['lName']
        self.user_name = data['username']
        self.password = data['pass']