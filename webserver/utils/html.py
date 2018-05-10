from __future__ import absolute_import, print_function
import re
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    _space_regex = re.compile(r'[ ]+', flags=re.I)
    _paragraph_regex = re.compile(r'\n{3,}', flags=re.I)

    def __init__(self):
        self.reset()
        self.content = []

    def handle_starttag(self, tag, attrs):
        if tag == u'br':
            self.content.append(u'\n')
        if tag == u'p':
            self.content.extend([u'\n', u'\n'])
        HTMLParser.handle_starttag(self, tag, attrs)

    def handle_startendtag(self, tag, attrs):
        if tag == u'br':
            self.content.append(u'\n')
        if tag == u'p':
            self.content.extend([u'\n', u'\n'])
        HTMLParser.handle_startendtag(self, tag, attrs)

    def handle_data(self, data):
        self.content.append(data)

    def get_data(self):
        content = self.content
        # remove spaces around sentences
        # use a regexp so we don't destroy lone \n's
        content = map(lambda line: line.strip(), content)
        # replace double-spaces with single space
        content = map(lambda line: self._space_regex.sub(u' ', line), content)
        # join into a single string with spaces
        content = u' '.join(content)
        # replace 3 or more new lines with a double new line
        content = self._paragraph_regex.sub(u'\n\n', content)
        # strip newlines at start and end incase it was enclosed in tags
        content = content.strip()
        return content


def strip_html(html):
    s = MLStripper()
    # unescape any html chars
    html = s.unescape(html)
    s.feed(html)
    return s.get_data()
