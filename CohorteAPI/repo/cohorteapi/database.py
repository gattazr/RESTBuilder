#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, Property, Validate, Invalidate, Requires
# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
# Abstract class and methods
from abc import ABCMeta, abstractmethod

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    """
    Create an abstract declarative meta for the declarative base. That way, Model classes will be able to inherit an abstract class and the declarative base
    """
    pass

@ComponentFactory("cohorteapi.database_factory")
@Provides("cohorteapi.database")
class Database(object):
    """
    Database handler
    """

    def __init__(self):
        """
        Initialisation of the database handler
        """
        # TODO: log creation of engine, base and session maker
        # TODO: get infos from a config file (import cohorte to get path ot config folder)
        wEngine = 'sqlite:////Users/gattazr/development/cohorte/applications/cohorte-licences/cohorte-licences/storage/database.db'

        self._engine = create_engine(wEngine)
        self._base = declarative_base(metaclass=DeclarativeABCMeta)
        self._sessionmaker = sessionmaker(bind=self._engine, expire_on_commit=False)

    def session(self):
        """
        Return a newly created session on the database
        """
        # TODO: log creation of session
        wDBSession = self._sessionmaker()
        return wDBSession

    def base(self):
        """
        Return the base (See sqlalchemy documentation)
        """
        return self._base

    def createAll(self):
        """
        Create the database using all previously created models extending the base (See sqlalchemy
        documentation)
        """
        # TODO: log create/update of tables in database
        self._base.metadata.create_all(self._engine)
