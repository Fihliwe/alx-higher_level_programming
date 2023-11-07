#!/usr/bin/python3
"""Defines a text file- reading function."""

def read_file(filename=""):
    """reads file and print to stdout"""

    with open(filename, encoding="UTF-8" as f:
            print(f.read(), end="")
