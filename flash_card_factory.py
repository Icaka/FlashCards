from flash_card import FlashCard
from flash_card_repository_json import FlashCardRepositoryJson


class FlashCardFactory:
    def __init__(self, repo: FlashCardRepositoryJson):
        self.repo_json = repo

    def create_card(self, side1: str, side2: str):
        temp_card = FlashCard(None, side1, side2)
        self.repo_json.insert(temp_card) # during insertion the card also receives its id
        return temp_card

    def create_bulk_cards(self):
        side1: str = None
        # side2: str = None
        while side1 != 'ex':
            print('Input side1: ')
            side1 = input()
            if side1 == 'ex':
                break
            print('Input side2: ')
            side2 = input()
            print('Created: ')
            print(self.create_card(side1, side2))
        print('End of bulk creation')
