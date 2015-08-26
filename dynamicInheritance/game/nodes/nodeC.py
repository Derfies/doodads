class NodeC( object ):

    inherits = ['NodeB']

    def __init__( self ):
        super( NodeC, self ).__init__()
        print 'NodeC init'

    def doSomething( self ):
        super( NodeC, self ).doSomething()

        print 'NodeC doSomething' 