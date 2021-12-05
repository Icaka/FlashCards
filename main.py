import json
from user import User
from user_repository import UserRepository
from user_repository_json import UserRepositoryJson

if __name__ == '__main__':
    #print_hi('PyCharm')
    with open("database.json") as d:
        data = json.load(d)

    print(data)

    repo_json = UserRepositoryJson()
    repo_json.load()
    # repo_json.print_all()
