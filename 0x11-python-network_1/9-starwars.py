#!/usr/bin/python3
"""
searches star wars API with string
"""
import requests
from sys import argv


if __name__ == "__main__":
    search = argv[1]
    url = 'https://swapi.co/api/people'

    req = requests.get(url, params={'search': search})
    results = req.json()

    print("Number of results: {}".format(results['count']))

    if results['count'] > 0:
        for i in results['results']:
            print(i['name'])
