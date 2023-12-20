from flash_card import FlashCard
from flash_card_repository import FlashCardRepository

class Category:
    def __init__(self, name):
        self.name = name
        self.id_list = []

    def add_card_id(self, card_id):
        if not card_id.isnumeric():
            return False
        if card_id in self.id_list:
            return False
        self.id_list.append(card_id)
        return True
    
    def add_card(self, card: FlashCard):
        return self.add_card_id(card.id)
    
    def get_name(self):
        return self.name
    
    def check_if_in(self, card_id):
        return card_id in self.id_list
    
    