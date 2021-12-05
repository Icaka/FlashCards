import json

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository

DEFAULT_CARDS_DB_FILE = "database.json"


class FlashCardRepositoryJson(FlashCardRepository):
    def __init__(self, filename=DEFAULT_CARDS_DB_FILE):
        super().__init__()
        self.db_file_name = filename

    def load(self):
        database = load_from_file(self.db_file_name)
        for c in database['flash_cards']:

            card = FlashCard()
            card.create_from_dict(c)
            # print(user)
            self.insert(card)


def load_from_file(filename):
    with open(filename, "rt") as f:
        return json.load(f)
