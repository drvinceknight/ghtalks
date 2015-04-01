import unittest

import ghtalks

import os

class TestTalks(unittest.TestCase):

    def test_init(self):
        talk = ghtalks.Talk('talk 1', '2015-04-01', './directory')
        self.assertEquals(talk.title, 'talk 1')
        self.assertEquals(talk.date, '2015-04-01')
        self.assertEquals(talk.path, './directory')
