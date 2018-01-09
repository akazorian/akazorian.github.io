#!/anaconda/bin/python

import argparse
import os
import re
from gen_file import *

def gen_link(File, link):
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

def gen_notes():
    pass

topic_map = {}
pattern = re.compile(".tex")
for dirpath, dirs, files in os.walk("notes/"):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        if pattern.search(fname):
            gen_file(File=fname, link=filename)
            topic = extract_topic(fname)
            if topic in topic_map:
                topic_map[topic] += (fname, filename)
            else:
                topic_map[topic] = (fname, filename)

for key, value in topic_map.items():
    print(key, value)

with open("notes/notes.html", 'w+') as note:
    with open("notes/template.html", 'r+') as temp:

