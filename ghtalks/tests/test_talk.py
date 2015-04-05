import unittest

import ghtalks

import os

class TestTalks(unittest.TestCase):

    def test_init(self):
        talk = ghtalks.Talk('talk 1', '2015-04-01', './directory', '.html')
        self.assertEquals(talk.title, 'talk 1')
        self.assertEquals(talk.date, '2015-04-01')
        self.assertEquals(talk.path, './directory')
        self.assertEquals(talk.file_type, '.html')

    def test_html(self):
        talk = ghtalks.Talk('talk 1', '2015-04-01', './directory/index.html', '.html')
        expected_out = """
<span class="post-date">2015-04-01 [.html]</span>\n<a class="post-link" href="./directory/index.html">talk 1</a>
"""
        self.assertEquals(talk.html(), expected_out)
