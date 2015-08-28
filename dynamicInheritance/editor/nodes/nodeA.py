class NodeA( object ):

    def __init__( self ):
        super( NodeA, self ).__init__()
        print 'NodeA EDITOR init'

    def doSomething( self ):
        super( NodeA, self ).doSomething()

        print 'NodeA EDITOR doSomething' 