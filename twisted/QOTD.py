#!/usr/bin/env python2
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import *
from twisted.internet import reactor

class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()

factory = Factory()
factory.protocol = QOTD

endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(factory)
reactor.run()
