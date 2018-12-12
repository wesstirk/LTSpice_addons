import globals as glb

def terminal_help():
    for com in glb.commands.keys() :
        print(com, ": ", glb.commands[com][glb.HELP_INDEX])

