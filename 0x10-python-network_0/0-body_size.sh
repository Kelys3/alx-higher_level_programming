#!/bin/bash
# Takes in a url, sends a request and displays the size of the body in bytes
curl -s "$1" | wc -c
