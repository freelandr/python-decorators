"""
module doc string
"""
import sys

import requests

print(sys.version)
print(sys.executable)

r = requests.get('https://coreyms.com')
print(f'status code = {r.status_code}')


def main(myvar: int):
    """ function doc string """
    print(myvar)


main(10)
