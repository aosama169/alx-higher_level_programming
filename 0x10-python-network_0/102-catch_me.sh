#!/bin/bash
# Make request to catch_me and get the message got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
