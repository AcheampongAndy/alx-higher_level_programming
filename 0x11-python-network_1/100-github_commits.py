#!/usr/bin/python3
""" Write a Python script that takes 
2 arguments in order to solve this challenge."""
import requests
import sys

if __name__ == "__main__":
    repos_name = sys.argv[1]
    username = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            username, repos_name)

    r = requests.get(url)
    json_data = r.json()

    try:
        for x in range(min(10, len(json_data))):
            print('{}: {}'.format(
                json_data[x].get('sha'),
                json_data[x].get('commit').get('author').get('name')))
    except IndexError:
        pass
