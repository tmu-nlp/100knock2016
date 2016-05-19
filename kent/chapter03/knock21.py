#!/usr/bin/python
#_*_coding:utf-8_*_

import json
import re
from knock20 import get_UK_text


def extract_category():
    for line in get_UK_text().split("\n"):
        if "Category" in line:
            print line


if __name__ == "__main__":
    extract_category()

