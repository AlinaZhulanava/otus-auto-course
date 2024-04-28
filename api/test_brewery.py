import pytest
import requests
from api.Breweries import Bre

URL = "https://api.openbrewerydb.org/v1/breweries"

countries = ["United States",
             "Ireland"]

filters = ["by_city",
           "by_dist",
           "by_ids",
           "by_name",
           "by_state",
           "by_postal",
           "by_type"
           ]

test_data_for_filters = {"by_city": "Cincinnati",
                         "by_dist": "32.88313237,-117.1649842",
                         "by_ids": "701239cb-5319-4d2e-92c1-129ab0b3b440",
                         "by_name": "San Diego",
                         "by_state": "California",
                         "by_postal": "92101",
                         "by_type": "micro"}

bre = Bre()
site = bre.brew_site_generator(requests.get(URL))


@pytest.mark.parametrize("country", countries)
def test_find_breweries_from_country_in_main_list(country):
    response = requests.get(URL)
    assert response.status_code == 200
    assert bre.filter_by(response, "country", country) is not None


@pytest.mark.parametrize("filter", filters)
def test_filter_breweries(filter):
    response = requests.get(URL, {filter: test_data_for_filters[filter]})
    assert response.status_code == 200
    assert bre.get_breweries_list(response) is not None


@pytest.mark.parametrize("site", site)
def test_working_brew_website(site):
    response = requests.get(site)
    assert response.status_code == 200


@pytest.mark.parametrize("count", [1, 2, 49, 50])
def test_random_brewery_size_param(count):
    response = requests.get(URL + '/random', {"size": count})
    assert response.status_code == 200
    assert len(bre.get_breweries_list(response)) == count


def test_metadata_total_is_positive():
    response = requests.get(URL + "/meta")
    assert bre.get_total_from_meta(response) > 0
