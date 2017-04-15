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
import javalang
import os

# Main Function
#===================================================#
def main(argv):

    # Generate the report
    filename = parse_uml()
    generateUML(filename)

# Methods
#===================================================#
def parse_uml():

    directory = './SourceFiles/uml-parser-test-1'
    # Parse all files from directory
    treeArray = get_trees_from_dir(directory)

    for file in treeArray:
        # Class Level
        # here we create the class boxes with fields or methods names
        for clas in file.types:
            print(clas.modifiers)
            print(clas.name)
            print(clas.extends)
            print(clas.implements)
            print(clas.body)
#           Iterract thru body elements
            for element in clas.body:
                print(element.modifiers)
                print(element.type)

                print("END OF CLASS")



def generateUML(filename):
    pass

# Setup and Initiation
#===================================================#
def usage():
    print('usage: umlparser.py <source folder> <output file name>')
    print('example: python3 umlparser.py /dir/Test.java /output/test.png')
    exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])

# Helper functions
#===================================================#
def get_trees_from_dir(directory):
    # parse a compilation unit from a string

    # Variable to hold trees from files in directory
    treeArray = []

    # Walk the directory passed into the function
    for dirpath, dnames, files in os.walk(directory):
        for file in files:

            # Check if the file is a '.java' file
            if file.endswith(".java"):
                # Parse and store tree in array
                treeArray.append(javalang.parse.parse(open(directory+'/' + file, 'r').read()))

    return treeArray


