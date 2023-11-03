#!/bin/bash
# Sends a POST request to a URL with custom variables, displays response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
