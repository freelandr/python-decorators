"""
module doc string
"""
import sys

import requests

print(sys.version)
print(sys.executable)

r = requests.get('https://coreyms.com')
print(r.status_code)
i = 10
i = 'mystring'


def main(myvar: int):
    """ function doc string """
    print(myvar)


main(10)
