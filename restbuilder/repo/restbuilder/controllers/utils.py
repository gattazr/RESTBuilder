#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""
# request parser
from urllib.parse import parse_qs
# import functions used to decode
from codecs import decode

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

def pathToParts(aPath):
    """
    Remove the prefix and suffix / if they exist and return the path splitted on '/'

    :param aPath: path to split

    :return: Splitted path on '/'
    """
    wPath = str(aPath)
    if wPath[0] == '/':
        wPath = wPath[1:]
    if wPath[-1] == '/':
        wPath = wPath[:-1]

    return wPath.split('/')

def parseBody(aRequest):
    """
    Parse the body of a given request and return a dictionnary of all its values

    :param aRequest: Request handler

    :return: a dictionnary
    """
    wData = decode(aRequest.read_data(), 'UTF-8')
    return parse_qs(wData)
