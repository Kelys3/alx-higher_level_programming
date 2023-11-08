#!/usr/bin/python3
"""
This script takes your GitHub username and personal access token (as password)
and uses the GitHub API to display your user id.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    auth = (username, password)

    response = requests.get(url, auth=auth)
    user_data = response.json()
    user_id = user_data.get('id')
    print("{}".format(user_id))
