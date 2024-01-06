#!/usr/bin/python3
""" script that takes in a URL and an email address, sends a POST request """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    r = requests.post(url, data=data)
    print(r.text)
