import game
import nodes


class Base( game.Base ):
    
    def __init__( self, *args, **kwargs ):
		self.nodeMgr = nodes.Manager()