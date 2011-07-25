#!/usr/bin/env python2
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import *
from twisted.internet import reactor

class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write(self.factory.quote + '\r\n')
        self.transport.loseConnection()

class QOTDFactory(Factory):

    protocol = QOTD

    def __init__(self, quote = None):
        self.quote = quote or "An apple a day keeps the doctor away"

reactor.listenTCP(8007, QOTDFactory("configurable quote"))
reactor.run()
