import json


class Bre():
    def __init__(self):
        pass

    def get_total_from_meta(self, response):
        meta = json.loads(response.text)
        return int(meta["total"])

    def get_breweries_list(self, response):
        breweries = json.loads(response.text)
        if not breweries:
            return None
        return breweries

    def brew_site_generator(self, response):
        generator = (brewery["website_url"]
                     for brewery in self.get_breweries_list(response)
                     if brewery["website_url"] is not None)
        return generator

    def filter_by(self, response, filter, value):
        breweries = []
        for brewery in self.get_breweries_list(response):
            if brewery[filter] == value:
                breweries.append(brewery)
        if not breweries:
            return None
        return breweries
