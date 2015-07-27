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
        crwl.crawl_directories(os.path.join(root, 'examples'))
        self.assertEquals(sorted(crwl.directories), [os.path.join(root, d)
                          for d in
                          ['examples/2015-04-05-Organise-and-share-talks',
                                    'examples/archive/2014-12-25-Auraya',
                                    'examples/archive/2015-07-27-links']])

    def test_has_date(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        self.assertTrue(crwl.has_date('2015-03-04'))
        self.assertTrue(
            crwl.has_date(os.path.join(root, '2015-12-04-directory')))
        self.assertFalse(
            crwl.has_date(os.path.join(root, '2015-12-32-directory')))
        self.assertFalse(
            crwl.has_date(os.path.join(root, '15-12-04-directory')))
        self.assertFalse(
            crwl.has_date(os.path.join(root, '1983-13-04-directory')))
        self.assertFalse(crwl.has_date(os.path.join(root, 'directory')))
        self.assertFalse(
            crwl.has_date(os.path.join(root, 'directory_2015-12-04')))

    def test_generate_talks(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'examples'))
        talks = crwl.generate_talks()
        talk_titles = sorted([t.title for t in talks])
        talk_dates = sorted([t.date for t in talks])
        talk_paths = sorted([t.path for t in talks])
        self.assertEqual(talk_titles,
                         ['Auraya', 'Organise and share talks', 'links'])
        self.assertEqual(talk_dates, ['2014-12-25', '2015-04-05', '2015-07-27'])
        self.assertEqual(talk_paths,
                         ['./examples/2015-04-05-Organise-and-share-talks/index.html',
                          './examples/archive/2014-12-25-Auraya/index.pdf',
                          'http://vknight.org/Talks/\n'])
