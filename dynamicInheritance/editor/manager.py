import inspect

import nodes
from game import nodes as gameNodes
from game.manager import Manager as GameManager


class Manager( GameManager ):

    def build( self ):
        eClsMap = self.getBaseClasses( nodes )
        gClsMap = self.getBaseClasses( gameNodes )
        
        # Compile classes.
        for clsName in sorted( gClsMap.keys() ):
            bases = []
            baseName = clsName
            while True:
                if baseName in eClsMap:
                    bases.append( eClsMap[baseName] )
                bases.append( gClsMap[baseName] )

                if not hasattr( gClsMap[baseName], 'inherits' ):
                    break
                baseName = getattr( gClsMap[baseName], 'inherits' )[0]

            self.addNodeWrapper( clsName, bases, {} )

        for k, v in self.nodeWrprs.items():
            print k, v
            for el in inspect.getmro( v ):
                print '    ', el