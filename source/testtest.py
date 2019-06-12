
import globals as glb
import ltspice_session

def test(params=None) :
    ltspice_session.UpdatePids()


def test2(params=None) :
    print(glb.currentFile)