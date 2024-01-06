#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) """
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(username, password))

    json_data = r.json()
    try:
        print(json_data['id'])
    except KeyError:
        print('None')
