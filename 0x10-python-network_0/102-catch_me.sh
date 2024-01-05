#!/bin/bash
# Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes
curl -s -X PUT -L -d "user_id=98" -H "Origin: HobertonSchool" 0.0.0.0:5000/catch_me
