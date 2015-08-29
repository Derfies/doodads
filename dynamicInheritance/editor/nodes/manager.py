from game.nodes.manager import Manager as GameManager


class Manager( GameManager ):

    def build( self, gameNodes, edNodes ):
        gClsMap = self.getBaseClasses( gameNodes )
        eClsMap = self.getBaseClasses( edNodes )

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