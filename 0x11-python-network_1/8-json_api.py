#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to """
import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=data)

    try:
        json_data = r.json()
        if json_data == {}:
            print('No result')
        else:
            print('[{}] {}'.format(json_data.get('id'), json_data('name')))
    except ValueError:
        print('Not a valid JSON')
