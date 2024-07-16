import json
import pytest
import requests
from api.PathProvider import get_path

PATH_USER11 = get_path("user11.json")

URL = "https://jsonplaceholder.typicode.com"
USERS_COUNT = 10


def test_post_users_successful():
    with open(PATH_USER11, "r") as f:
        response = requests.post(URL+"/users", f)
    assert response.status_code == 201
    assert int(json.loads(response.text)["id"]) == 11


def test_get_users_successful():
    response = requests.get(URL + "/users")
    users = json.loads(response.text)
    assert response.status_code == 200
    assert len(users) == USERS_COUNT


def test_cant_delete_posts():
    response = requests.get(URL + "/posts")
    assert response.status_code == 200
    posts = json.loads(response.text)
    posts_size_before_delete = len(posts)
    post_to_delete = posts[-1]

    response = requests.delete(URL + "/posts/" + str(len(posts) - 1))
    assert response.status_code == 200

    response = requests.get(URL + "/posts")
    posts = json.loads(response.text)
    assert len(posts) == posts_size_before_delete
    assert posts[-1] == post_to_delete


def find_users_item(user, items):
    find_result = False
    for item in items:
        if user["id"] == item["userId"]:
            find_result = True
            break
    return find_result


@pytest.mark.parametrize("item", ["posts", "todos", "albums"])
def test_all_users_have(item):
    response = requests.get(URL + "/users")
    users = json.loads(response.text)

    response = requests.get(URL + "/" + item)
    items = json.loads(response.text)

    for user in users:
        if find_users_item(user, items) is False:
            assert False
    assert True


@pytest.mark.parametrize("endpoint", ["posts", "todos", "photos"])
def test_all_titles_are_unique(endpoint):
    response = requests.get(URL + "/" + endpoint)
    items_list = json.loads(response.text)
    items_set = {item["title"] for item in items_list}
    assert len(items_list) == len(items_set)
