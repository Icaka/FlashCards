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

    def to_json(self):
        return self.__dict__

    def create_from_dict(self, data):
        id = data['id']
        tries = data['tries']
        success = data['success']
