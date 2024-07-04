#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -sLI "$1" | grep "Allow" | cat -d " " -f 2-
