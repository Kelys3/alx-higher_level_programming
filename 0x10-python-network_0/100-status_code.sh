#!/bin/bash
# Sends a request to a given URL, displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
