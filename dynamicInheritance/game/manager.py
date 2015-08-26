import sys
import types
import inspect

import nodes


class Manager( object ):

    def __init__( self, *args, **kwargs ):
        self.nodeWrprs = {}

        self.build()

        #print inspect.getmembers( nodes, inspect.isclass )
        #print dir( nodes )
        #print getattr( nodes, 'nodeA' )

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

    def build( self ):

        clsMap = self.getBaseClasses( nodes )
        
        # Compile classes.
        for clsName, cls in clsMap.items():
            base = cls
            mro = [base]
            methods = {}
            while hasattr( base, 'inherits' ):
                base = clsMap[getattr( base, 'inherits' )[0]]       # TODO: Support multiple inheritance.
                mro.append( base )
                methods.update( {
                    k: v
                    for k, v in base.__dict__.items()
                    if isinstance( v, types.FunctionType )
                } )

            print 'MAKE CLASS:', clsName
            print 'mro:', mro
            print 'meth', methods
            cls = type( clsName, tuple( mro ), {'doSomething': mro[0].doSomething} )
            self.nodeWrprs[clsName] = cls
            obj = cls()
            obj.doSomething()


if __name__ == '__main__':
    nm = Manager()