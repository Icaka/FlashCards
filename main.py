import json
from user import User
from user_repository import UserRepository

if __name__ == '__main__':
    #print_hi('PyCharm')
    with open("database.json") as d:
        data = json.load(d)

    print(data)
    # print(data['users'])
    # print(data['users']['5'])
    # print(data['users']['5']['fName'])
    u1 = User()
    u2 = User()
    print(u1)
    u1.create_from_dict(data['users']['5'])
    u2.create_from_dict((data['users']['10']))
    print(u1)
    repo = UserRepository()
    repo.insert(u1)
    repo.insert(u2)
    print(repo.find_by_id(5))
    print(repo.find_by_id(10))
