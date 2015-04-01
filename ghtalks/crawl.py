"""
Crawl a given directory to find files of required type
"""
import os

import re

class Crawl:
    """
    A class for the complete crawl of a directory
    """
    def __init__(self, directory='.'):
        root = os.getcwd()
        self.directory = os.path.join(root, directory)

    def crawl_directories(self, directory):
        #self.directories = [f for f in os.walk(directory)]
        self.directories = [f for f in os.walk(directory) if os.path.isdir(f)]
        print self.directories
        #self.directories = [f for f in os.walk(directory) if (os.path.isdir(f) and self.has_date(f)]

    def has_date(self, directory):
        # Below is a regex for a date in ISO global date format
        regex = '(19|20)\d\d[- ./](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
        return bool(re.search(regex, directory))
