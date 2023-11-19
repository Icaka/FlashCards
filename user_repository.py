from user import User
from icecream import ic


class UserRepository:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, users={}, ):
        self.users = users

    def find_by_id(self, id):
        return self.users[id]

    def find_by_username(self, user_name):
        for u in self.users.values():
            if u.user_name == user_name:
                return u
        return None

    def insert(self, user: User):
        temp_id = 0
        print(f'inserting  {user}')
        if user.id is None:  # case for when a user is added manually and has no id yet
            temp_id = self.__class__.get_next_id()
        else:  # this case is for when the users are read from the db
            temp_id = user.id

        while temp_id in self.users:  # if there is already such id in users dict, gets the next id
            temp_id = self.__class__.get_next_id()

        user.id = temp_id
        self.users[user.id] = user
        return user

    def update(self, user: User):
        self.users[user.id] = user
        return user

    def delete_by_id(self, id):
        removed = self.users[id]
        del self.users[id]
        return removed

    def count(self):
        return len(self.users)

    def print_all(self):
        print('Users:')
        for user in self.users:
            print(self.users[user])
