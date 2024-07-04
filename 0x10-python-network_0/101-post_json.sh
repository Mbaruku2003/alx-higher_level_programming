#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -SL -H "Content-Type: Application/json" -d "$(cat "$2")" "$1"
