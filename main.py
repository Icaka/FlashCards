import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson

if __name__ == '__main__':
    with open("database.json") as d:
        data = json.load(d)

    print(data)

    users_json = UserRepositoryJson()
    users_json.load()
    users_json.print_all()
    cards = FlashCardRepositoryJson()
    cards.load()
    # cards.print_all()
