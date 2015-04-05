import unittest

import ghtalks

import os

class TestIndex(unittest.TestCase):


    expected_output="""
<body>\n<div class="page-content">\n<div class="wrap">\n<div class="home">\n<ul class=\'posts\'>\n<li>\n<span class="post-date">2015-04-01 [.html]</span>\n<a class="post-link" href="./ghtalks/tests/test_directory/test_subdirectory/2015-04-01-test-directory/index.html">test directory</a>\n\n</li>\n<li>\n<span class="post-date">2015-03-31 [.html]</span>\n<a class="post-link" href="./ghtalks/tests/test_directory/2015-03-31-test-directory-2/index.html">test directory 2</a>\n\n</li>\n<li>\n<span class="post-date">2015-03-30 [.pdf]</span>\n<a class="post-link" href="./ghtalks/tests/test_directory/2015-03-30-test-directory-1/index.pdf">test directory 1</a>\n\n<p><a href=dummyurl.com>screencast</a></p>\n\n</li>\n</ul>\n</div>\n</div>\n</div>\n\n</body>\n"""

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
                ['./ghtalks/tests/test_directory/2015-03-30-test-directory-1/index.pdf',
                 './ghtalks/tests/test_directory/2015-03-31-test-directory-2/index.html',
                 './ghtalks/tests/test_directory/test_subdirectory/2015-04-01-test-directory/index.html'])

    def test_generate_output(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'ghtalks/tests'))
        index = ghtalks.Index(crwl.generate_talks())
        index.generate_output()

        self.assertEqual(index.out, self.expected_output)

    def test_write(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'ghtalks/tests'))
        index = ghtalks.Index(crwl.generate_talks())
        index.generate_output()
        index.write()
        self.assertEqual(open('index.html', 'r').read(), self.expected_output)
        os.remove('index.html')
