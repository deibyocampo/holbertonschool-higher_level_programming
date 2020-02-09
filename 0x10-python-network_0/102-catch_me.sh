#!/bin/bash
#makes a request to 0.0.0.0:5000
curl 0.0.0.0:5000/catch_me -sLX PUT -d "user_id=98" -H "Origin: :HolbertonSchool"
