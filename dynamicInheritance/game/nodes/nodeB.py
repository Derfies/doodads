class NodeB( object ):

    inherits = ['NodeA']

    def __init__( self ):
        super( NodeB, self ).__init__()
        print 'NodeB init'

    def doSomething( self ):
        super( NodeB, self ).doSomething()

        print 'NodeB doSomething' 