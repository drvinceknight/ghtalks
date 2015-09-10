"""
Data holder for a talk
"""
import yaml


class Talk:
    def __init__(self, title, date, path, file_type, urls=None):
        self.title = title
        self.date = date
        self.path = path
        self.file_type = file_type
        self.urls = urls

    def html(self):
        out = """
<span class="post-date">%s [%s]</span>
<a class="post-link" href="%s">%s</a>
""" % (self.date, self.file_type, self.path, self.title)
        if self.urls:
            out += "<div class='urls'>"
            out += "<ul>"
            urls = yaml.load(open(self.urls, 'r'))
            for key in sorted(urls.keys()):
                out += """
<li><a href=%s>%s</a></li>""" % (urls[key], key)
            out += "</ul>"
            out += "</div>"
        return out
