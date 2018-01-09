#!/anaconda/bin/python

import argparse
import os
import re
from gen_file import *

topic_header = "<div class=\"col-sm-6\">\n<h1>{}:</h1>\n<ul class=\"nav flex-column\">\n"
topic_close = "</ul>\n</div>\n"
link_template = "<li class=\"nav-item\"><a href={}>{}</a></li>"

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
            if topic not in topic_map:
                topic_map[topic] = []
            topic_map[topic].append((fname.replace(".tex", ".html"), filename.replace(".tex", ".html")))

start_flag = re.compile("append here")
with open("notes/notes.html", 'w+') as note:
    with open("notes/template.html", 'r+') as temp:
        for line in temp:
            note.write(line)
            if start_flag.search(line):
                for key, value in topic_map.items():
                    note.write(topic_header.format(key))
                    for pair in value:
                        file_name, link = pair
                        note.write(link_template.format(file_name, link))
                    note.write(topic_close)
