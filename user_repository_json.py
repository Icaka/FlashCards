import json

from user import User
from user_repository import UserRepository

DEFAULT_USERS_DB_FILE = "database.json"


class UserRepositoryJson(UserRepository):
    def __init__(self, filename=DEFAULT_USERS_DB_FILE):
        super().__init__()
        self.db_file_name = filename

    def load(self):
        users_list = load_from_file(self.db_file_name)
        for u in users_list['users']:
            user = User()
            user.create_from_dict(u)
            # print(user)
            self.insert(user)


def load_from_file(filename):
    with open(filename, "rt") as f:
        return json.load(f)