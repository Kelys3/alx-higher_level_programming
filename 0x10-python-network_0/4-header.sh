#!/bin/bash
# Sends a GET request to a URL with a custom header, displays response body
curl -s -H "X-School-User-Id: 98" "$1"
