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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Build website.")
    parser.add_argument('build', help="Options include: notes,...")
    flag = parser.parse_args()
    build(flag.build)