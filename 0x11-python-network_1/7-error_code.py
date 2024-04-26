#!/usr/bin/python3
"""sends request to the URL displays body of response
"""
import sys
import requests


if __name__ == "__main__":
    urls = sys.argv[1]

    r = requests.get(urls)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
