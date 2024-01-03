from dataclasses import dataclass
from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson

# represents the way the user will store personal info(tries and successes) about a specific card in the db


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
        # print(f'data: {data}')
        self.id = data['id']
        self.tries = data['tries']
        self.success = data['success']
