#!/usr/bin/python3
"""
searches star wars API with string
"""
import requests
from sys import argv


if __name__ == "__main__":
    search = argv[1]
    url = url_first = 'https://swapi.co/api/people'

    while url is not None:
        req = requests.get(url, params={'search': search})
        results = req.json()

        if url == url_first:
            print("Number of results: {}".format(results['count']))
        for i in results['results']:
            print(i['name'])
            for film in i['films']:
                movie_info = requests.get(film).json()
                title = movie_info['title']
                print("\t{}".format(title))
        url = results['next']
