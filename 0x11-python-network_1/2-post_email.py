#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
