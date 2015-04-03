import unittest

import ghtalks

import os

class TestIndex(unittest.TestCase):

    def test_init(self):
        index = ghtalks.Index()
        self.assertEquals(index.directory, directory)
