#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and 
displays the value of the X-Request-Id variable found in the header of the response
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        result = response.info()
        print(result.get("X-Request-Id"))
