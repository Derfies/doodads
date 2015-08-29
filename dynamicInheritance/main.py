import game
import editor


if __name__ == '__main__':

    gm = game.Base()
    gm.nodeMgr.build( game.nodes )
    gm.nodeMgr.nodeWrprs['NodeC']()
    
    ed = editor.Base()
    ed.nodeMgr.build( game.nodes, editor.nodes )
    ed.nodeMgr.nodeWrprs['NodeC']()
    