import unittest

import ghtalks

import os

class TestIndex(unittest.TestCase):


    expected_output="""
<body>\n<div class="page-content">\n<div class="wrap">\n<div class="home">\n<ul class=\'posts\'>\n<li>\n<span class="post-date">2015-07-27 [.link]</span>\n<a class="post-link" href="http://vknight.org/Talks/\n">links</a>\n\n</li>\n<li>\n<span class="post-date">2015-04-05 [.html]</span>\n<a class="post-link" href="./examples/2015-04-05-Organise-and-share-talks/index.html">Organise and share talks</a>\n\n<p><a href=http://lab.hakim.se/reveal-js/#/>(slides written in reveal.js)</a></p>\n\n<p><a href=https://github.com/drvinceknight/ghtalks>github repository</a></p>\n\n</li>\n<li>\n<span class="post-date">2014-12-25 [.pdf]</span>\n<a class="post-link" href="./examples/archive/2014-12-25-Auraya/index.pdf">Auraya</a>\n\n</li>\n</ul>\n</div>\n</div>\n</div>\n\n</body>\n"""

    def test_init(self):
        root = os.getcwd()
        crwl = ghtalks.Crawl()
        crwl.crawl_directories(os.path.join(root, 'examples'))
        index = ghtalks.Index(crwl.generate_talks())
        talk_titles = sorted([t.title for t in index.talks])
        talk_dates = sorted([t.date for t in index.talks])
        talk_paths = sorted([t.path for t in index.talks])
        self.assertEqual(talk_titles, ['Auraya', 'Organise and share talks',
            'links'])
        self.assertEqual(talk_dates, ['2014-12-25', '2015-04-05', '2015-07-27'])
        self.assertEqual(talk_paths,
                ['./examples/2015-04-05-Organise-and-share-talks/index.html',
                    './examples/archive/2014-12-25-Auraya/index.pdf',
                    'http://vknight.org/Talks/\n'])

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
