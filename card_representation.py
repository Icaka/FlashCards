from dataclasses import dataclass
from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson


@dataclass
class CardRepresentation:
    id: int
    tries: int
    success: int

    def __str__(self):
        return f'{self.id}: {self.tries}, {self.success}'
    # def __init__(self, _id: int, tries: int, success: int):
    #     self.id = _id
    #     self.tries = tries
    #     self.success = success
