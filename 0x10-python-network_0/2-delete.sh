#!/bin/bash
# Sends DELETE request to URL as first argument, displays body of the response
curl -sX DELETE "$1"
