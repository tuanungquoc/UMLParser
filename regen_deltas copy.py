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

import agate
import csv
import fnmatch
import os
import sys
import re
import xml.etree.ElementTree as ET
import zipfile
import logging
import logging.config

# CSV file columns

def usage():
    print('usage: umlparser.py <source folder> <output file name>')
    print('example: python3 umlparser.py /dir/Test.java /output/test.png')
    exit(1)

# Main
def main(argv):

    # SETUP Logger
    if (os.environ['DEBUG'] == 'True'):
        # Load Logger Conf for Debugging.
        # if we are Debuggin set output to console too
        logging.config.fileConfig('logging_debug.conf', disable_existing_loggers=False)
    else:
        # Load Logger Conf for Production.
        logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

    # LOGGER Instantiation:  This has to be done in every module to allow logging
    logger = logging.getLogger(__name__)

    # Parse parameters
    if len(argv) == 2:
        source = os.path.abspath(argv[0])
        output = os.path.abspath(argv[1])
    else:
        usage()

    # Generate the report
    parse_uml(source, output)

if __name__ == "__main__":
    main(sys.argv[1:])

def parse_uml(self,source,output):
    # LOGGER Instantiation:  This has to be done in every module to allow logging
    logger = logging.getLogger(__name__)
    logger.info("Received source and output:"+source + output)
    pass