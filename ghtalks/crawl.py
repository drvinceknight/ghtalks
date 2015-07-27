"""
Crawl a given directory to find files of required type
"""
import os
import glob

import re
import talk


class Crawl:

    """
    A class for the complete crawl of a directory
    """

    def __init__(self, directory='.'):
        self.root = os.getcwd()
        self.directory = os.path.join(self.root, directory)
        # Below is a regex for a date in ISO global date format
        self.date_regex = '(19|20)\d\d[- ./](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'

    def crawl_directories(self, directory):
        self.directories = [f[0] for f in os.walk(directory) if
                            (os.path.isdir(f[0]) and self.has_date(f[0]))]

    def has_date(self, directory):
        return bool(re.search(self.date_regex,
            os.path.basename(os.path.normpath(directory))[:len('yyyy-mm-dd')]))

    def generate_talks(self, filetypes=['.pdf', '.html', '.link'],
                       talk_filename='index'):
        self.talks = []
        for d in self.directories:
            d = d[len(self.root):]
            try:
                tlk = [f for f in glob.glob('.' + d + '/' + talk_filename +
                    '.*') if any(ext in f for ext in filetypes)][0]
                raw_title, extension = os.path.splitext(tlk)
                date = re.search(self.date_regex, d).group()
                title = os.path.basename(d)[len(date) + 1:].replace("-", " ")

                urls = None
                if os.path.isfile('.' + d + '/urls.yml'):
                    urls = '.' + d + '/urls.yml'

                if extension in filetypes:
                    path = '.' + d + '/' + talk_filename + extension
                    if extension == '.link':
                        with open(path, 'r') as f:
                            path = f.read()
                    self.talks.append(
                        talk.Talk(title, date,
                                  path,
                                  extension, urls))
            except:
                pass
        return self.talks
