#!/usr/bin/python3
"""
Display 10 commits of the repository
"""


import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))

    commit = req.json()
    for commit in commit[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
