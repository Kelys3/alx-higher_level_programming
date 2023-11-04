#!/usr/bin/python3
"""
This script accepts a url as argument, sends a request to the url
and displays the value of `X-Request-Id` found in the header of the
response
"""
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    value = response.getheader('X-Request-Id')
    print("{}".format(value))


if __name__ == "__main__":
    pass
