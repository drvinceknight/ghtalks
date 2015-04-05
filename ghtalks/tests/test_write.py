import unittest

import ghtalks

import os

class TestIndex(unittest.TestCase):

    def test_init(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'ghtalks/tests'))
        index = ghtalks.Index(crwl.generate_talks())
        talk_titles = sorted([t.title for t in index.talks])
        talk_dates = sorted([t.date for t in index.talks])
        talk_paths = sorted([t.path for t in index.talks])
        self.assertEqual(talk_titles, ['test directory', 'test directory 1',
            'test directory 2'])
        self.assertEqual(talk_dates, ['2015-03-30', '2015-03-31', '2015-04-01'])
        self.assertEqual(talk_paths,
                ['/ghtalks/tests/test_directory/2015-03-30-test-directory-1/index.pdf',
                 '/ghtalks/tests/test_directory/2015-03-31-test-directory-2/index.html',
                 '/ghtalks/tests/test_directory/test_subdirectory/2015-04-01-test-directory/index.html'])
