#!/bin/bash
# Sends a JSON POST request with a file content as $2 to a URL as $1
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
