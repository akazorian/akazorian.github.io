import argparse
import os
import re
from gen_file import *

def build(flag):
    if flag == "notes":
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build website.")
    parser.add_argument('build', help="Options include: notes,...")
    flag = parser.parse_args()
    build(flag.build)