#!/usr/bin/python3
"""This script imports requests to fetch https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.content)))
    print("\t- content: {}".format(res.content))
