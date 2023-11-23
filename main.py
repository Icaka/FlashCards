import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson
# from icecream import ic

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson
from card_representation import CardRepresentation
from flash_card_controller import FlashCardController
from user_controller import UserController
from user_registration import UserRegistration

from quiz_controller import QuizController
from flash_card_factory import FlashCardFactory

if __name__ == '__main__':
    with open("database.json") as d:
        data = json.load(d)

    # print(data)
    # ic(data)

    users_json = UserRepositoryJson()
    users_json.load()
    # users_json.print_all()
    cards = FlashCardRepositoryJson()
    cards.load()
    # card1 = FlashCard(None, 'red', 'rot')
    # card2 = FlashCard(15, 'fear', 'angst')
    # cards.insert(card1)
    # cards.insert(card2)
    card_factory = FlashCardFactory(cards)
    card_factory.create_bulk_cards()
    cards.persist()
    cards.print_all()

    # user1 = User(10, 'koce', 'koce', 'koce', 'koce')
    # quiz_c = QuizController(cards, user1)
    # quiz_c.create_set_first_20()
    # quiz_c.quiz_on_current_set()
    # quiz_c.quiz_on_current_set()
    # user1.print_tried_cards()

    # card1 = FlashCard(15, 'good', 'dog')
    # card2 = FlashCard(20, 'bad', 'cat')
    # user1 = User(10, 'koce', 'koce', 'koce', 'koce')
    # # print(user1)
    # user1.guess_flash_card(card1, 'dog')
    # # user1.print_tried_cards()
    # user1.guess_flash_card(card1, 'boy')
    # # user1.print_tried_cards()
    # user1.guess_flash_card(card2, 'cat')
    # # user1.print_tried_cards()
    #
    # reg_toni = UserRegistration('toni', 'toni', 'ton', 'ton')
    # syst = UserController(users_json)
    # syst.register(reg_toni)
    #
    # users_json.insert(user1)
    # users_json.print_all()
    #
    # users_json.persist()
    user_test = User(None, 'joe', 'benson', 'jj', '12345')
    user_test2 = User(51, 'dany', 'torrance', 'dan51', '42red')
    users_json.print_all()
    users_json.insert(user_test)
    users_json.insert(user_test2)
    users_json.print_all()
    users_json.persist()
    # cards.print_all()
