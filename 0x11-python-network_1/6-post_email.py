#!/usr/bin/python3
"""this script takes in URL and email as arguments, sends POST requests
to given URL with email as parameter, displays body of response"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    res = requests.post(url, data=payload)
    print("{}".format(res.text))
