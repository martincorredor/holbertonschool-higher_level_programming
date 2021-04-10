#!/usr/bin/python3
"""
Module that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
from requests.auth import HTTPBasicAuth
import requests
from sys import argv
if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=HTTPBasicAuth(str(argv[1]), str(argv[2])))
    try:
        data = response.json()
        print(data["id"])
    except:
        print("None")
