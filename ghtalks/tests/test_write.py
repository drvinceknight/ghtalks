import unittest

import ghtalks

import os

class TestIndex(unittest.TestCase):


    expected_output="""
<body>\n<div class="page-content">\n<div class="wrap">\n<div class="home">\n<ul class=\'posts\'>\n<li>\n<span class="post-date">2015-04-05 [.html]</span>\n<a class="post-link" href="./examples/2015-04-05-Using-ghtalks-to-organise-your-talks/index.html">Using ghtalks to organise your talks</a>\n\n</li>\n<li>\n<span class="post-date">2014-12-25 [.pdf]</span>\n<a class="post-link" href="./examples/archive/2014-12-25-Auraya/index.pdf">Auraya</a>\n\n</li>\n</ul>\n</div>\n</div>\n</div>\n\n</body>\n"""

    def test_init(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'examples'))
        index = ghtalks.Index(crwl.generate_talks())
        talk_titles = sorted([t.title for t in index.talks])
        talk_dates = sorted([t.date for t in index.talks])
        talk_paths = sorted([t.path for t in index.talks])
        self.assertEqual(talk_titles, ['Auraya', 'Using ghtalks to organise your talks'])
        self.assertEqual(talk_dates, ['2014-12-25', '2015-04-05'])
        self.assertEqual(talk_paths, ['./examples/2015-04-05-Using-ghtalks-to-organise-your-talks/index.html', './examples/archive/2014-12-25-Auraya/index.pdf'])

    def test_generate_output(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'examples'))
        index = ghtalks.Index(crwl.generate_talks())
        index.generate_output()

        self.assertEqual(index.out, self.expected_output)

    def test_write(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'examples'))
        index = ghtalks.Index(crwl.generate_talks())
        index.generate_output()
        index.write()
        self.assertEqual(open('index.html', 'r').read(), self.expected_output)
        os.remove('index.html')
