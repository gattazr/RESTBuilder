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
# json
import json
# os
import os

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

    def session(self):
        """
        Return a newly created session on the database
        """
        wDBSession = self._sessionmaker()
        _logger.info('Creation of database session : %r', wDBSession)
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

    @Validate
    def validate(self, aContext):
        """
        Initialisation of the database component
        """
        _logger.debug('Validating DB')

        # Loading the config
        wConfig = {}
        wBasePath = aContext.get_property('cohorte.base')
        _logger.debug('Base path : ', wBasePath)

        wConfigFilePath = os.path.join(wBasePath, "conf/cohorteapi/database.js")
        _logger.debug('database config file : %s', wConfigFilePath)
        # Read the json file
        with open(wConfigFilePath) as wConfigFile:
            wConfig = json.load(wConfigFile)
        _logger.debug('Config : %s', wConfig)


        # setting up the component
        self._engine = create_engine(wConfig['connexion_string'])
        _logger.info('Creation of engine : %r', self._engine)
        self._base = declarative_base(metaclass=DeclarativeABCMeta)
        _logger.info('Creation of base : %r', self._base)
        self._sessionmaker = sessionmaker(bind=self._engine, expire_on_commit=False)
        _logger.info('Creation of datatbase sessions provider : %r', self._sessionmaker)
