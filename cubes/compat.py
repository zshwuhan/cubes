# -*- encoding: utf-8 -*-
"""Pytho compatibility utilities"""

from __future__ import absolute_import

import sys

py3k = sys.version_info >= (3, 0)

if py3k:
    string_type = str
    binary_type = bytes
    text_type = str
    int_types = int,
    iterbytes = iter

    from urllib.parse import urlparse
    from urllib.request import urlopen
    import configparser
    from io import StringIO
    from queue import Queue

else:
    string_type = basestring
    binary_type = str
    text_type = unicode
    int_types = int, long

    from urlparse import urlparse
    from urllib2 import urlopen
    import ConfigParser as configparser
    from StringIO import StringIO
    from Queue import Queue

