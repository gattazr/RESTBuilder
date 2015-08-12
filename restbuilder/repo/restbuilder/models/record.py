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
import datetime
import time
# sqlalchemy
from sqlalchemy import Column, TIMESTAMP

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

class AbstractRecord(metaclass=ABCMeta):
    """
    Abstract Record
    """

    created_at = Column(TIMESTAMP(), nullable=False)
    updated_at = Column(TIMESTAMP(), nullable=False)

    def dict(self, aFilter=utils.defaultFilter):
        """
        Create a dictionnary representing the current object by filtering the object __dict__

        :param aFilter: predicate used on the __dict__ keys to filter the dictionnary
        :return: a dictionnary
        """
        # TODO: test 'blob' wValue
        wDict = self.__dict__
        wDateTypes= (datetime.date, datetime.datetime)
        wExported = {}
        for wKey, wValue in wDict.items():
            if(aFilter(wKey)):
                # If the value is an AbstractRecord
                if issubclass(wValue.__class__, AbstractRecord):
                    wExported[wKey] = wValue.dict(aFilter)

                # If the value is a Date
                elif issubclass(wValue.__class__, wDateTypes):
                    # Make a real timestamp
                    wExported[wKey] = int(time.mktime(wValue.timetuple()))

                # Otherwise
                else:
                    wExported[wKey] = wValue

        return wExported
