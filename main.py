import json
from user import User

if __name__ == '__main__':
    #print_hi('PyCharm')
    with open("database.json") as d:
        data = json.load(d)

    print(data)
    # print(data['users'])
    # print(data['users']['5'])
    # print(data['users']['5']['fName'])
    u1 = User()
    print(u1)
    u1.create_from_dict(data['users']['5'])
    print(u1)
