#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""

# Abstract class and methods
from abc import ABCMeta, abstractmethod
# import utils functions
import restbuilder.models.utils as utils

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

class AbstractFacilities(metaclass=ABCMeta):
    """
    Abstract Facilities
    """

    @abstractmethod
    def getRecord(self):
        pass

    @abstractmethod
    def __makeTableDef__(self):
        pass
