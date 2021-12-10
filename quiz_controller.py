from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson
from flash_card_controller import FlashCardController
from user_controller import UserController
from quiz import Quiz


class QuizController:
    def __init__(self, flash_card_repo: FlashCardRepository, logged_user: User):
        self.flash_card_repo = flash_card_repo
        self.logged_user = logged_user
        self.quiz_set: list(FlashCard) = []

    def create_set_first_20(self):
        self.quiz_set.clear()
        count = 20
        if self.flash_card_repo.count() <= 20:
            count = self.flash_card_repo.count()
        iterat = 0
        for card in self.flash_card_repo.flash_cards:
            self.quiz_set.append(self.flash_card_repo.flash_cards[card])
            # print(self.flash_card_repo.flash_cards[card])
            iterat += 1
            if iterat >= count:
                break

        for c in self.quiz_set:
            print(c)

    def quiz_on_current_set(self):
        current_quiz = Quiz(self.logged_user, self.quiz_set)
        current_quiz.iterate_quiz()


