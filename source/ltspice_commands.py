import globals as glb

def terminal_help():
    for com in glb.helpInfo.keys() :
        print(com, ": ", glb.helpInfo[com])

    if (len(glb.helpInfo) != len(glb.commands)) :
        print("Warning: Help info is incomplete")
