#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -ILs "$1" | greep Allow | cut -d " " -f2-
