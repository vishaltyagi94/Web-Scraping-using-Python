#!/usr/bin/env/python
"""
__author__ = "Vishal Tyagi"
"""
import urllib.request
from bs4 import BeautifulSoup

for i in range(3, 110):
    url = "https://www.physionet.org/pn4/eegmmidb/S" + "{:03d}".format(i) +"/"
    htmlfile = urllib.request.urlopen(url)
    html = htmlfile.read()
    soup = BeautifulSoup(html, features="html.parser")
    for tag in soup.findAll('a'):
        if str(tag.get('href')).startswith("S"+"{:03d}".format(i)):
            # TODO Write Download Code


