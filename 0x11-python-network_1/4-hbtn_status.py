#!/usr/bin/pyhton3
"""Module for  Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    response = request.get("https://alx-intranet.hbtn.io/status")
    print(Body response:)
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text)
