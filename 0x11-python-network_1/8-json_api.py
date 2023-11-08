#!/usr/bin/python3
"""This script takes a letter as an argument, sends POST request to
http://0.0.0.0:5000/search_user with the letter as parameter"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}

    res = requests.post(url, data=payload)

    try:
        json_data = res.json()

        if json_data == {}:
            print("No result")
        else:
            print("[{}]) {}".format(json_data['id'], json_data['name']))
    except ValueError:
        print("Not a valid JSON")
