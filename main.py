import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository

if __name__ == '__main__':
    with open("database.json") as d:
        data = json.load(d)

    print(data)

    repo_json = UserRepositoryJson()
    repo_json.load()

    flash1 = FlashCard()
    flash1.create_from_dict(data['flash_cards'][0])
    flash2 = FlashCard()
    flash2.create_from_dict(data['flash_cards'][1])
    flash_repo = FlashCardRepository()
    flash_repo.insert(flash1)
    flash_repo.insert(flash2)
    flash_repo.print_all()
    # repo_json.print_all()
