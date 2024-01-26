#!/usr/bin/python3
"""Module script that takes in a URL, sends a request to the URL"""
import sys
import requests


if __name__ == "__main__":
    responses  = requests.get(sys.argv[1])
    print(responses.headers.get("X-Request-Id"))
