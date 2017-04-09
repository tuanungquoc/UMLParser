#!/usr/local/bin/python3
# umlparser.py
# Author: Carlos Martinez
#
# Overview:
# Input:
#   <source folder>
#   <output file name>
# Output:
#   Class Diagram in png format

import sys
import plyj.parser as plyj
import os

# CSV file columns

def usage():
    print('usage: umlparser.py <source folder> <output file name>')
    print('example: python3 umlparser.py /dir/Test.java /output/test.png')
    exit(1)

def parse_uml():

    # parse a compilation unit from a string
    parser = plyj.Parser()

    treeArray = []
    for dirpath, dnames, files in os.walk("./uml-parser-test-1/"):
        for file in files:
            if file.endswith(".java"):
                treeArray.append(parser.parse_file('./uml-parser-test-1/'+file))

    print("Tree: " + str(treeArray))

# Main
def main(argv):

    # Generate the report
    parse_uml()

if __name__ == "__main__":
    main(sys.argv[1:])




