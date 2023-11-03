#!/bin/bash
# Takes URL as input and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | grep Allow | cut -d ' ' -f 2-
