#!/usr/bin/python3
"""
This script takes in a url and email as arguments, sends a POST
request to the given url with the email as parameter and
displays the decoded(utf-8) body of response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req)as response:
        page = response.read().decode('utf-8')
        print("{}".format(page))
