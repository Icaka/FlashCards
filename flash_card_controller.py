from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson


class FlashCardController:
    def __init__(self, flash_repository: FlashCardRepository):
        self.flash_repo = flash_repository

    def create_card(self, side_1, side_2):
        new_card = FlashCard(FlashCardRepository.get_next_id(), side_1, side_2)
        self.flash_repo.insert(new_card)