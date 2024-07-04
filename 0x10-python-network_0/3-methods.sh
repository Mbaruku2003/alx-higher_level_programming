#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -sLI "$1" | cut -d " " -f | grep "Allow"
