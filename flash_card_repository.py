class FlashCardRepository:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, flash_cards={}, ):
        self.flash_cards = flash_cards

    def find_by_id(self, id):
        return self.flash_cards[id]

    def insert(self, flash_card):
        # flash_card.id = self.__class__.get_next_id()
        self.flash_cards[flash_card.id] = flash_card
        return flash_card

    def update(self, flash_card):
        self.flash_cards[flash_card.id] = flash_card
        return flash_card

    def delete_by_id(self, id):
        removed = self.flash_cards[id]
        del self.flash_cards[id]
        return removed

    def count(self):
        return len(self.flash_cards)

    def print_all(self):
        for flash_card in self.flash_cards:
            print(self.flash_cards[flash_card])
            