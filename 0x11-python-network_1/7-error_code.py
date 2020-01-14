#!/usr/bin/python3
"""
takes in a URL
"""
import requests
import sys


if __name__ == "__main__":
    """
    func definition
    """
    req = requests.get(sys.argv[1])
    if req.status_code == 200:
        print(req.text)
    else:
        print("Error code:", req.status_code)
