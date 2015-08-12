#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""
import time

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

def prepareMessage():
    """
    Create a dictionnary that contains the default informations of a message

    :return : a dictionnary
    """
    wDict = {}
    wHeaders = {}
    wMetadata = {}

    wHeaders['timestamp'] = int(time.time())

    wDict['headers'] = wHeaders
    wDict['metadata'] = wMetadata
    return wDict
