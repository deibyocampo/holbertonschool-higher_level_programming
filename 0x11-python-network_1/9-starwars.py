#!/usr/bin/python3
"""
searches star wars API with string
"""
import sys
import requests


if __name__ == "__main__":
    search = {'search': sys.argv[1]}
    req = requests.get('https://swapi.co/api/people', params=search)
    results = req.json()
    count = results.get('count')
    print("Number of results: {}".format(count))
    for i in results.get('results'):
        print(i.get('name'))
