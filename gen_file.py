import argparse
import os
import subprocess
import string
import re

relative_path = os.getcwd()
nav = '<li><a href="#{}">{}</a></li>\n'

def gen_file(File=None, FULLPATH=None, O=None):
    if FULLPATH != None:
        gen_helper(FULLPATH)
    else:
        gen_helper(File)

def gen_helper(File):
    with open("temp.html", 'w+') as html:
        with open("template.html", 'r+') as temp:
            output = subprocess.check_output(["pandoc", "--from", "latex", "--to", "html5", "--mathjax", File])
            pattern = re.compile("<article class=\"markdown-body\">")
            for line in temp:
                html.write(line)
                if pattern.match(line):
                    html.write(output.decode("utf-8"))

    with open("temp.html", 'r+') as html:
        ids, headers, depth, lines = set_up_nav_bar(html)

    gen_nav(File, ids, headers, depth, lines)
    os.remove("temp.html")

def set_up_nav_bar(File):
    header = re.compile("<h\\d")
    extract_id = re.compile('\"(.+?)\"')
    extract_header = re.compile(">(.+)<")
    extract_depth = re.compile("<h(\\d)")
    ids = []
    headers = []
    depth = []
    lines = []
    for line in File:
        lines.append(line)
        if header.search(line) != None:
            curr_id = extract_id.search(line)
            ids.append(curr_id.groups(0)[0])
            curr_head = extract_header.search(line)
            headers.append(curr_head.groups(0)[0])
            curr_depth = extract_depth.search(line)
            depth.append(int(curr_depth.groups(0)[0]))
    return ids, headers, depth, lines

def gen_nav(File, ids, headers, depth, lines):
    pattern = re.compile("<body>")
    with open(File.replace(".tex", ".html"), 'w+') as html:
        for line in lines:
            html.write(line)
            if pattern.match(line):
                html.write('<div id="mySidenav" class="sidenav">\n<nav>\n<ul>\n')
                curr_depth = depth[0]
                for i in range(len(ids)):
                    temp_depth = depth[i]
                    if temp_depth == curr_depth + 1:
                        html.write('<ul>\n')
                    elif temp_depth < curr_depth:
                        for j in range(curr_depth - temp_depth):
                            html.write('</ul>\n')
                    curr_depth = temp_depth
                    html.write(nav.format(ids[i], headers[i]))
                html.write('</ul>\n</nav>\n</div>\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a webpage for a LaTex file.")
    parser.add_argument('--file', help="Name of TeX file in relative path for which a webpage will be produced.")
    parser.add_argument('--fullpath', help="If provided, then file at the provided path will be used to generate a webpage.")
    parser.add_argument('--o', help="Optional name of output file.")
    args = parser.parse_args()
    gen_file(File=args.file, FULLPATH=args.fullpath, O=args.o)