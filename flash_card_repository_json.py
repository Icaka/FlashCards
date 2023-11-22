import json

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository

DEFAULT_CARDS_DB_FILE = "database.json"
DEFAULT_CARDS_DB_SAVE_FILE = 'databases/flash_cards.json'


class FlashCardRepositoryJson(FlashCardRepository):
    def __init__(self, filename=DEFAULT_CARDS_DB_FILE):
        super().__init__()
        self.db_file_name = filename

    def load(self):
        database = load_from_file(self.db_file_name)
        for c in database['flash_cards']:

            card = FlashCard()
            card.create_from_dict(c)
            self.insert(card)
    
    def persist(self):
        cards = list(map(lambda c: c.to_json(), self.flash_cards.values()))
        with open(DEFAULT_CARDS_DB_SAVE_FILE, 'wt') as f:
            json.dump(cards, f, indent=4)


def load_from_file(filename):
    with open(filename, "rt") as f:
        return json.load(f)
