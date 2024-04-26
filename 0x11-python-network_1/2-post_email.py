#!/usr/bin/python3
"""take URL and send POST request to the passed URL
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    reqUrl = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(reqUrl, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
