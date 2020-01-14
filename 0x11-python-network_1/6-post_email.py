#!/usr/bin/python3
"""
POST an email
"""
import requests
import sys


if __name__ == "__main__":
    """
    func definition
    """
    data = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=data)
    print(req.text)
