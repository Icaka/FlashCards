import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson
from user_registration import UserRegistration

from flash_card import FlashCard
from flash_card_repository import FlashCardRepository
from flash_card_repository_json import FlashCardRepositoryJson


class UserController:
    def __init__(self, user_repository: UserRepository):
        self.name = 'system'
        self.currently_logged = False
        self.currently_logged_user = User()
        self.user_repository = user_repository

    # def start(self):
    #     if not self.currently_logged:

    def login(self, user_name, password):
        user: User = self.user_repository.find_by_username(user_name)
        if user is None:
            return False
        if user.password == password:
            self.currently_logged = True
            self.currently_logged_user = user
            # self.currently_logged_user.create_from_dict(u)
        return self.currently_logged

    def register(self, user_reg: UserRegistration):
        new_user = User(0, user_reg.f_name, user_reg.l_name, user_reg.user_name, user_reg.password)
        self.user_repository.insert(new_user)
#
