#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
:authors: Rémi GATTAZ
:copyright: Copyright 2015, IsandlaTech
:license:  Apache Software License 2.0
"""
# cohorte
import cohorte
# Abstract class and methods
from abc import ABCMeta, abstractmethod
# json
import json
# View utils
import cohorteapi.views.utils as utils

# Version information
__version_info__ = (0, 0, 1)
__version__ = ".".join(str(x) for x in __version_info__)

# Logging
import logging
_logger = logging.getLogger(__name__)

class AbstractView(metaclass=ABCMeta):
    """
    Abstract view
    """

    def show404(self, aResponse):
        """
        Return an empty message with a 404 HTTP-code

        :param aReponse: Response handler
        """
        self.showMessage(aResponse, 404, '')

    def show200(self, aResponse):
        """
        Return an empty message with a 200 http code

        :param aReponse: Response handler
        """
        self.showMessage(aResponse, 200, '')

    def redirect(self, aResponse, aCode, aPath):
        """
        Send a redirection message
        """
        aResponse.set_header('content-type', "application/json")
        aResponse.set_header('Location', aPath)
        wMessage = utils.prepareMessage()
        aResponse.send_content(aCode, json.dumps(wMessage))

    def showMessage(self, aResponse, aCode, aMessage):
        """
        Display a message

        :param aReponse: Response handler
        :param aCode: http-code of the response
        :param aMessage: a message
        """
        aResponse.set_header('content-type', "application/json")
        wMessage = utils.prepareMessage()
        wMessage['content'] = aMessage
        aResponse.send_content(aCode, json.dumps(wMessage))


    def showError(self, aResponse, aCode, aException):
        """
        Display an error message containing the exception message. The exception is also logged

        :param aReponse: Response handler
        :param aCode: http-code of the response
        :param aException: the exception
        """
        # Trace the exception in the log
        _logger.exception("Exception : %s", aException)

        aResponse.set_header('content-type', "application/json")
        wMessage = utils.prepareMessage()
        wMessage['content'] = str(aException.orig)
        aResponse.send_content(aCode, json.dumps(wMessage))
