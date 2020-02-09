#!/usr/bin/python3
"""
takes in a letter
"""
import requests
import sys


if __name__ == "__main__":
    """
    func definition
    """
    if len(sys.argv) > 1:
        letter = sys.argv[1]
        req = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    if len(sys.argv) == 1:
        req = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})

    try:
        json_dict = req.json()
        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.json()["id"], req.json()["name"]))
    except ValueError:
        print("Not a valid JSON")
