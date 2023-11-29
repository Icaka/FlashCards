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

    def get_currently_logged_user(self) -> User:
        if self.currently_logged is False:
            return None
        return self.currently_logged_user
    # def start(self):
    #     if not self.currently_logged:

    def login(self, user_name, password):
        user: User = self.user_repository.find_by_username(user_name)
        if user is None:
            return False
        if user.password != password:
            return False
        self.currently_logged = True
        self.currently_logged_user = user
        # self.currently_logged_user.create_from_dict(u)
        return self.currently_logged

    def logout(self):
        self.currently_logged_user = User()
        self.currently_logged = False

    def register(self, user_reg: UserRegistration):
        if not user_reg.f_name.strip() or not user_reg.l_name.strip():  # checking for empty input
            return False
        if self.user_repository.find_by_username(user_reg.user_name):
            return False
        new_user = User(None, user_reg.f_name, user_reg.l_name, user_reg.user_name, user_reg.password)
        self.user_repository.insert(new_user)
        return True

    def print_all_users(self):
        self.user_repository.print_all()
#
