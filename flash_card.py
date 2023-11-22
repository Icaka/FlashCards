class FlashCard:
    def __init__(self, _id=None, side1=None, side2=None):
        self.id = _id
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f"{self.id}: {self.side1} | {self.side2}"

    def create_from_dict(self, data):
        self.id = data['id']
        self.side1 = data['side1']
        self.side2 = data['side2']
    
    def to_json(self):
        return self.__dict__
