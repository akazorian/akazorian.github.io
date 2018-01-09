#!/anaconda/bin/python

import argparse
import os
import re
from gen_file import *

pattern = re.compile(".tex")
for dirpath, dirs, files in os.walk("notes/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        if pattern.search(fname):
            gen_file(File=fname, link=filename)
            gen_link(File=fname, link=filename)

def gen_link(File, link):
    print(File, link)
    topic = extract_topic(File)
    print(topic)
    with open("notes/notes.html", 'w+') as home:
         home.write("<a href={}> {}</a>\n".format(File.replace(".tex", ".html"), link))

def extract_topic(File):
    topic = ""
    for c in File[6:]:
        if c == "/":
            break
        topic += c
    return topic