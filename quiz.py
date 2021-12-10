from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson
from flash_card_controller import FlashCardController
from user_controller import UserController


class Quiz:
    def __init__(self, logged_user: User, quiz_set):
        self.logged_user = logged_user
        self.quiz_set = quiz_set
        self.successful_guesses = 0

    def iterate_quiz(self):
        for c in self.quiz_set:
            print(c.side1)
            user_guess = input('Enter your guess: ')
            if self.logged_user.guess_flash_card(c, user_guess):
                print('T')
                self.successful_guesses += 1
            else:
                print('F')

