import nodes
from game.manager import Manager as GameManager


class Manager( GameManager ):

    def __init__( self ):
        GameManager.__init__( self )
        print self.getBaseClasses( nodes )