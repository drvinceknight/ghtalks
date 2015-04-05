"""
Script to write the html
"""
import crawl

class Index:
    """
    Class that is passed a list of talks and writes the required html
    """
    def __init__(self, talks, css_dir = False):
        self.talks = talks
