"""
Script to write the html
"""
import crawl

class Index:
    """
    Class that is passed a list of talks and writes the required html
    """
    def __init__(self, talks, head=None, header=None, footer=None):
        self.talks = talks
        self.head = head
        self.header = header
        self.footer = footer

    def generate_output(self):
        self.out = """"""
        for f in [self.head, self.header]:
            try:
                self.out += open(f, 'r').read()
            except:
                pass
        self.out += """
<body>
<div class="page-content">
<div class="wrap">
<div class="home">
<ul class='posts'>"""
        for talk in sorted(self.talks, key=lambda x: x.date, reverse=True):
            self.out += """
<li>"""
            self.out += talk.html()
            self.out += """
</li>"""
        self.out += """
</ul>
</div>
</div>
</div>
"""
        if self.footer:
            self.out += open(self.footer, 'r').read()
        self.out += """
</body>
"""

    def write(self, output_file='index.html'):
        f = open(output_file, 'w')
        f.write(self.out)
        f.close()
