import json


def read_users(file_users):
    users = json.loads(file_users.read_file())  # returns a list of objects
    filtered_users = []
    for user in users:
        user_dict = {"name": user["name"], "gender": user["gender"], "address": user["address"], "age": user["age"],
                     "books": []}
        filtered_users.append(user_dict)
    return filtered_users
