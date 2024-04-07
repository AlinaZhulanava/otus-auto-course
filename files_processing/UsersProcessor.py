import json


def read_users(file_users):
    users = json.loads(file_users.read())  # returns a list of objects
    filtered_users = []
    for user in users:
        user_dict = {"name": user["name"], "gender": user["gender"], "address": user["address"], "age": user["age"],
                     "books": []}
        filtered_users.append(user_dict)
    return filtered_users

def write_users(file_result, users_with_books):
    piece_of_json = json.dumps(users_with_books)
    file_result.write(piece_of_json)