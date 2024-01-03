import json

from user import User
from user_repository import UserRepository
# from icecream import ic

DEFAULT_USERS_DB_FILE = "database.json"
DEFAULT_USERS_DB_SAVE_FILE = "databases/users.json"
TEST_DB_LOCATION = "databases/users_test.json"


class UserRepositoryJson(UserRepository):
    def __init__(self, filename=DEFAULT_USERS_DB_FILE):
        super().__init__()
        self.db_file_name = filename

    def load(self):
        users_list = load_from_file(self.db_file_name)['users']  # load_from_file() returns the whole json db
        for u in users_list:
            user = User()
            user.create_from_dict(u)
            # print(user)
            self.insert(user)
        # ic(self.users)

    def persist(self):
        new_users = list(map(lambda u: u.to_json(), self.users.values()))
        save_to_file(TEST_DB_LOCATION, new_users)


def load_from_file(filename):
    with open(filename, "rt") as f:
        return json.load(f)


def save_to_file(filename, users):
    """Save users data to JSON file"""
    with open(filename, "wt") as f:
        json.dump(users, f, indent=4)
