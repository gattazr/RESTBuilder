#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""

# sqlalechmy
from sqlalchemy import TIMESTAMP

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

class TableDefinition(object):
    """
    Description of a Table in the database
    """
    def __init__(self, aName):
        self.name = aName
        self._columns = {}
        self._relations = {}

        self.addColumn(ColumnDefinition('created_at', TIMESTAMP, aNullable=False))
        self.addColumn(ColumnDefinition('updated_at', TIMESTAMP, aNullable=False))

    def addColumn(self, aColumn):
        """
        Add a column to the table. Raise an exception if aColumn is not a subclass of ColumnDefinition
        :param aColumn: Column to add
        """
        # TODO: Raise exception
        if issubclass(aColumn.__class__, ColumnDefinition):
            self._columns[aColumn.name] = aColumn
        # else:
        #     raise exception, not a Column

    def addRelation(self, aRelation):
        """
        Add a relation to the table. Raise an exception if aColumn is not a subclass of ColumnDefinition
        :param aRelation: Relation to add
        """
        # TODO: Raise exception
        if issubclass(aRelation.__class__, RelationDefinition):
            self._relations[aRelation.name] = aRelation
        # else:
        #     raise exception, not a relation

    def __repr__(self):
        return "<%s(name=%s, columns=%r, relations=%r)>" % (self.__class__.__name__, self.name, self._columns, self._relations)


class ColumnDefinition(object):
    """
    Description of a Column in a Table
    """
    def __init__(self, aName, aType, aPrimaryKey=False, aForeignKey=None, aNullable=True, aUnique=False, aImmutable=False):
        # TODO: check the functions type
        self.name = aName
        self.type = aType
        self._primaryKey = aPrimaryKey
        self._foreignKey = aForeignKey
        self._nullable = aNullable
        self._unique = aUnique
        self._immutable = aImmutable

    def isPrimaryKey(self):
        """
        Return True if the column is the columns is part of the primary key. False otherwise
        :return: bolean
        """
        return self._primaryKey

    def isForeignKey(self):
        """
        Return a string containg the Table name and the Column name this Column is linked to if the column is a foreign key. None otherwise

        :return: None or a string following the given format : 'TableName.ColumnName'
        """
        return self._foreignKey
    def isNullable(self):
        """
        Return True if the column can be NULL. False otherwise
        :return: boolean
        """
        if self.isPrimaryKey():
            return False
        else:
            return self._nullable
    def isUnique(self):
        """
        Return True if the column has a UNIQUE constraint. False otherwise
        :return: boolean
        """
        if self.isPrimaryKey():
            return True
        else:
            return self._unique
    def isImmutable(self):
        """
        Return True if the Column can not be modified after it was set. False otherwise
        :return: boolean
        """
        if self.isPrimaryKey():
            return True
        else:
            return self._immutable

    def __repr__(self):
        return "<%s(name=%s, type=%r, isPrimaryKey=%r, isForeignKey=%r, isNullable=%r, isUnique=%r, isImmutable=%r)>" % (self.__class__.__name__, self.name, self.type, self.isPrimaryKey(), self.isForeignKey(), self.isNullable(), self.isUnique(), self.isImmutable())

class RelationDefinition(object):
    """
    Description of a relation
    """

    def __init__(self, aName, aTarget, aBackRef=None, aOrder=None):
        self.name = aName

        self._target = aTarget
        self._backref = aBackRef
        self._order = aOrder
        # TODO: How to describe Many to Many relations ?

    def getTarget(self):
        """
        Return the relation target

        :return: Target of the relation
        """
        return self._target

    def getOrder(self):
        """
        Return the name of the column of the target used to sort the elements retrieved with the relation

        :return: name of the column of the target used to sort the elements retrieved with the relation
        """
        return self._order

    def getBackref(self):
        """
        Return the name of the fields to use for the backref

        :return: name of the fields to use for the backref
        """
        return self._backref

    def __repr__(self):
        return "<%s(target=%s, order=%s, backref=%s)>" % (self.__class__.__name__, self.getTarget(), self.getOrder(), self.getBackref())
