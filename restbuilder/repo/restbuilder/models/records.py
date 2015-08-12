#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Requires
# sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
# Abstract
from restbuilder.models.record import AbstractRecord

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)


@ComponentFactory("restbuilder.records_factory")
@Requires("_db", "restbuilder.database")
@Provides("restbuilder.records")
class Records(object):
    """
    Handler of the classes mapping the database
    """

    def __init__(self):
        self._recordClasses = {}

    def getRecordClass(self, aClassName):
        """
        Return the record class associated to the name

        :param aClassName: name of the record class to retrieve
        :return: Record classe
        """
        return self._recordClasses[aClassName]

    def registerRecordClass(self, aRecordClass):
        """
        add a Record class

        :param aRecordClass: Class Record to add
        """
        if issubclass(aRecordClass, AbstractRecord):
            _logger.info('registering Record : %s', aRecordClass.__name__)
            self._recordClasses[aRecordClass.__name__] = aRecordClass
        else:
            # TODO: Raise an exception insted of this log
            _logger.error('%s is not not a Record class.', aRecordClass)


    def unregisterRecordClass(self, aRecordClassName):
        """
        add a Record class

        :param aRecordClassName: Name of the Class Record to remove
        """
        # TODO: remove from the metadata the table
        # self.db.base().metedata.remove(self._recordClasses[aRecordClassName])
        del self._recordClasses[aRecordClassName]
