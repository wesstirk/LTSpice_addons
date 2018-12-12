import terminal #just do it myself?
import globals as glb


while(True):
    command = terminal.prompt(" ", glb.DEFAULT_COMMAND)
    args = command.split(' ')

    #todo: pass in arguments into the function.
    if glb.commands.__contains__(args[0]) :
        glb.commands[args[0]][glb.FUNCTION_INDEX]()
    elif command != glb.DEFAULT_COMMAND :
        print("ERROR: Invalid Command")
        glb.commands['help'][glb.FUNCTION_INDEX]()
