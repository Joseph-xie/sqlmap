#!/usr/bin/env python

"""
$Id$

Copyright (c) 2006-2011 sqlmap developers (http://www.sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.common import Backend
from lib.core.datatype import AttribDict
from lib.core.settings import EXCLUDE_UNESCAPE

class Unescaper(AttribDict):
    def unescape(self, expression, quote=True, dbms=None):
        if expression is None:
            return expression

        for exclude in EXCLUDE_UNESCAPE:
            if exclude in expression:
                return expression

        identifiedDbms = Backend.getIdentifiedDbms()

        if dbms is not None:
            return self[dbms](expression, quote=quote)
        elif identifiedDbms is not None:
            return self[identifiedDbms](expression, quote=quote)
        else:
            return expression

unescaper = Unescaper()
