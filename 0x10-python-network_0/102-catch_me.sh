#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me and respond You got me!
curl -s 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool"
