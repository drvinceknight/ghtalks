import unittest

import ghtalks

import os

class TestCrawl(unittest.TestCase):

    def test_init(self):
        root = os.getcwd()
        directory = os.path.join(root, '.')
        crwl = ghtalks.Crawl()
        self.assertEquals(crwl.directory, directory)

        crwl = ghtalks.Crawl('a_directory')
        directory = os.path.join(root, 'a_directory')
        self.assertEquals(crwl.directory, directory)

    def test_crawl_directory(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'ghtalks/tests'))
        test_directories = [os.path.join(root, d) for d in
                                ['ghtalks/tests/test_directory/2015-03-30-test-directory-1',
                                 'ghtalks/tests/test_directory/2015-03-31-test-directory-2',
                                 'ghtalks/tests/test_directory/test_subdirectory/2015-04-01-test_directory']]
        self.assertEquals(sorted(crwl.directories), sorted(test_directories))

    def test_has_date(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        self.assertTrue(crwl.has_date('2015-03-04'))
        self.assertTrue(crwl.has_date(os.path.join(root, '2015-12-04-directory')))
        self.assertTrue(crwl.has_date(os.path.join(root,'directory_2015-12-04')))
        self.assertFalse(crwl.has_date(os.path.join(root,'2015-12-32-directory')))
        self.assertFalse(crwl.has_date(os.path.join(root,'15-12-04-directory')))
        self.assertFalse(crwl.has_date(os.path.join(root,'1983-13-04-directory')))
        self.assertFalse(crwl.has_date(os.path.join(root,'directory')))
