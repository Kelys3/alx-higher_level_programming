#!/usr/bin/python3
"""This script takes a URL as argument, sends requests to the URL and displays
the value of X-Request-Id in response header"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if 'X-Request-Id' in res.headers:
        print(res.headers.get("X-Request-Id"))
