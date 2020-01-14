#!/usr/bin/python3
"""
POST an email
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """
    func definition
    """
    data = {'email': sys.argv[2]}
    data = bytes(urllib.parse.urlencode(data).encode())
    with urllib.request.urlopen(sys.argv[1], data) as handler:
        print(handler.read().decode('utf-8'))
