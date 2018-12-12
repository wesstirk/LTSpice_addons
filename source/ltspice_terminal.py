import terminal #just do it myself?
import globals as glb

DEFAULT_COMMAND = " " # todo: make this const


while(True):
    command = terminal.prompt(" ", DEFAULT_COMMAND)
    args = command.split(' ')
    print(args)

    if glb.commands.__contains__(command) :
        glb.commands[command]()