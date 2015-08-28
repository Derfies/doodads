import game
import editor


if __name__ == '__main__':
    nm = editor.Manager()
    nm.build()

    nm.nodeWrprs['NodeC']()
    print '*****'
    nm = game.Manager()
    nm.build()

    nm.nodeWrprs['NodeC']()