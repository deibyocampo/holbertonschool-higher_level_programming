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
    if len(sys.argv) > 1:
        req = requests.get(sys.argv[1])
        print(req.headers.get("X-Request-Id"))
