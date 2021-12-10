import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson
from card_representation import CardRepresentation
from flash_card_controller import FlashCardController
from user_controller import UserController
from user_registration import UserRegistration

if __name__ == '__main__':
    with open("database.json") as d:
        data = json.load(d)

    print(data)

    users_json = UserRepositoryJson()
    users_json.load()
    users_json.print_all()
    # cards = FlashCardRepositoryJson()
    # cards.load()
    # cards.print_all()
    card1 = FlashCard(15, 'good', 'dog')
    card2 = FlashCard(20, 'bad', 'cat')
    user1 = User(10, 'koce', 'koce', 'koce', 'koce')
    print(user1)
    user1.guess_flash_card(card1, 'dog')
    user1.print_tried_cards()
    user1.guess_flash_card(card1, 'boy')
    user1.print_tried_cards()
    user1.guess_flash_card(card2, 'cat')
    user1.print_tried_cards()
    # reg_toni = UserRegistration('toni', 'toni', 'ton', 'ton')
    # syst = UserController(users_json)
    # syst.register(reg_toni)
    # users_json.print_all()

    # users_json.persist()
    # cards.print_all()
