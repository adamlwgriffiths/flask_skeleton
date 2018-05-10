from __future__ import absolute_import, print_function
import os

def generate_secret_key(size=32):
    return os.urandom(size)
