"""
Data holder for a talk
"""

class Talk:
    def __init__(self, title, date, path, file_type):
        self.title = title
        self.date = date
        self.path = path
        self.file_type = file_type

    def html(self):
        out = """
<span class="post-date">%s [%s]</span>
<a class="post-link" href="%s">%s</a>
""" % (self.date, self.file_type, self.path, self.title)
        return out
