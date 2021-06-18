import requests as re

def retrieve_list(url):

    """ This function simply retrieves a payload and outputs the name of beer that contains india and brewed after 2000"""
    resp = re.get(url)
    resp_range = range(len(resp.json()))
    final_list = []
    for i in resp_range:
        final_list.append(f"Beer Name: {resp.json()[i]['name']},  First Brewed: {resp.json()[i]['first_brewed']}")
    for element in final_list:
        print(element)
    return final_list


retrieve_list("https://api.punkapi.com/v2/beers?beer_name=india&brewed_after=12-2000")