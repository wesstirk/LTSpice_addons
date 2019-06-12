
import globals as glb

def test(params=None) :
    print("This is the test function")
    print("It doesn't do anything yet....")
    glb.currentFile = 'random.asc'

def test2(params=None) :
    print(glb.currentFile)