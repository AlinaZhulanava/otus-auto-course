import pytest
import requests
from api.Dogs import Dogs
from api.PathProvider import get_path

PATH_BREEDS_LIST = get_path("breeds_list.txt")
PATH_EXPECTED_SUB_BREEDS = get_path("sub_breeds_list.txt")

test_urls = ["https://dog.ceo/api/breeds/list/all",
             "https://dog.ceo/api/breeds/image/random", ]

dogs = Dogs()


@pytest.mark.parametrize("url", test_urls)
def test_breed_list_call(url):
    response = requests.get(url)
    assert response.status_code == 200
    assert dogs.get_status_from_body(response) == "success"
    assert dogs.get_message_from_body(response) != {}


@pytest.mark.parametrize("expected_breed",
                         dogs.get_expected_breeds(PATH_BREEDS_LIST))
def test_breeds_from_breed_list(expected_breed):
    url_dogs = test_urls[0]
    response = requests.get(url_dogs)
    breeds_dict = dogs.get_message_from_body(response)
    assert breeds_dict[expected_breed] is not None


@pytest.mark.parametrize("expected_breed_with_subbreed",
                         dogs.get_expected_breeds(PATH_EXPECTED_SUB_BREEDS))
def test_breed_has_attributes(expected_breed_with_subbreed):
    url_dogs = ("https://dog.ceo/api/breed/" +
                expected_breed_with_subbreed + "/list")
    response = requests.get(url_dogs)
    assert dogs.get_status_from_body(response) == "success"
    assert dogs.get_message_from_body(response) != []


def test_random_image():
    response = requests.get(test_urls[1])
    image_url = dogs.get_message_from_body(response)
    image_response = requests.get(image_url)
    assert image_response.status_code == 200


@pytest.mark.parametrize("number", [1, 2, 49, 50])
def test_random_images_amount(number):
    response = requests.get(test_urls[1]+'/'+str(number))
    image_urls_list = dogs.get_message_from_body(response)
    assert len(image_urls_list) == number
