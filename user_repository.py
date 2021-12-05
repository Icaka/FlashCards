class UserRepository:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, users = {}, ):
        self.users = users

    def find_by_id(self, id):
        return self.users[id]

    def insert(self, user):
        # user.id = self.__class__.get_next_id()
        self.users[user.id] = user
        return user

    def update(self, user):
        self.users[user.id] = user
        return user

    def delete_by_id(self, id):
        removed = self.users[id]
        del self.users[id]
        return removed

    def count(self):
        return len(self.users)

    def print_all(self):
        for user in self.users:
            print(self.users[user])
