from card_representation import CardRepresentation
from flash_card import FlashCard


class User:

    def __init__(self, _id=None, fName=None, lName=None, user_name=None, password=None):
        self.id = _id
        self.fName = fName
        self.lName = lName
        self.user_name = user_name
        self.password = password
        self.cardsInfo: list(CardRepresentation) = []   # TODO  also make the quiz

    def __str__(self):
        return f"{self.id}: {self.fName} {self.lName} -- {self.user_name}, {self.password}"

    def create_from_dict(self, data):
        self.id = data['id']
        self.fName = data['fName']
        self.lName = data['lName']
        self.user_name = data['username']
        self.password = data['pass']

    def add_card_info(self, card_representation: CardRepresentation):
        self.cardsInfo.append(card_representation)

    def update_card_info(self, card_id: int, success: bool):
        found: bool = False
        for r in self.cardsInfo:
            if card_id == r.id:
                found = True
                r.tries += 1
                if success:
                    r.success += 1
        if not found:
            new_card: CardRepresentation
            if success:
                new_card = CardRepresentation(card_id, 1, 1)
            else:
                new_card = CardRepresentation(card_id, 1, 0)
            self.add_card_info(new_card)

    def guess_flash_card(self, card: FlashCard, guess):
        # new_card: CardRepresentation = CardRepresentation(card.id, 0 , 0)
        # print('guess is here')
        if guess == card.side2:
            self.update_card_info(card.id, True)
            return True
        else:
            self.update_card_info(card.id, False)
            return False

    def print_tried_cards(self):
        for c in self.cardsInfo:
            print(c)

    def to_json(self):
        temp = self.__dict__
        temp['cardsInfo'] = list(map(lambda c: c.to_json(), self.cardsInfo))
        return temp
