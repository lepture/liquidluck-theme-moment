#!/usr/bin/env python


def tag_url(tag):
    from liquidluck.writers.base import content_url
    from liquidluck.options import settings
    prefix = settings.site.get('prefix', '')
    root = content_url(prefix, 'tag', 'index.html')
    return '%s#%s' % (root, tag)


def year_url(post):
    from liquidluck.writers.base import content_url
    from liquidluck.options import settings
    prefix = settings.site.get('prefix', '')
    return content_url(prefix, post.date.year, 'index.html')
