import types


class Manager( object ):

    def __init__( self, *args, **kwargs ):
        self.nodeWrprs = {}

    def getBaseClasses( self, mod ):
        """Get list of classes."""
        clsMap = {}
        for name in dir( mod ):
            el = getattr( mod, name )
            if not isinstance( el, types.ModuleType ):
                continue
            clsName = name[:1].upper() + name[1:]
            cls = getattr( el, clsName )
            clsMap[cls.__name__] = cls

        return clsMap

    def addNodeWrapper( self, clsName, mro, methods ):
        cls = type( clsName, tuple( mro ), methods )
        self.nodeWrprs[clsName] = cls

    def build( self, mod ):
        clsMap = self.getBaseClasses( mod )
        
        # Compile classes.
        for clsName in sorted( clsMap.keys() ):
            bases = []
            baseName = clsName
            while True:
                bases.append( clsMap[baseName] )

                if not hasattr( clsMap[baseName], 'inherits' ):
                    break
                baseName = getattr( clsMap[baseName], 'inherits' )[0]

            self.addNodeWrapper( clsName, bases, {} )


if __name__ == '__main__':
    nm = Manager()
    nm.getBaseClasses( None )