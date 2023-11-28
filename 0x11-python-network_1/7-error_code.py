#!/usr/bin/python3
"""This script takes in a URL as argument , sends request to the given URL
displays body of response"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print("{}".format(res.text))
