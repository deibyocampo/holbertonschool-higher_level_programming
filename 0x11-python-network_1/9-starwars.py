#!/usr/bin/python3
"""
searches star wars API with string
"""
import requests
from sys import argv


if __name__ == "__main__":
    search = argv[1]
    req = requests.get('https://swapi.co/api/people', params={'search': search})
    results = req.json()

    print("Number of results: {}".format(results['count']))

    if results['count'] > 0:
        for i in results['results']:
            print(i['name'])
