#!/usr/bin/python3
"""This script takes a letter as an argument, sends POST request to
http://0.0.0.0:5000/search_user with the letter as parameter"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {"q": letter}

    res = requests.post(url, payload)

    try:
        data = res.json()

        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError:
        print("Not a valid JSON")
