#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)


def defaultFilter(aString):
    """
    Predicate function

    :param aString: String to test

    :return: False if the given key starts with '_' or contains password. True otherwise
    """
    if(aString.startswith("_")):
        return False
    if('password' in aString):
        return False

    return True
