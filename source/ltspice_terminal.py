#Created by Wesley Stirk on December 11, 2018
#Last updated by Wesley Stirk on December 12, 2018
#This will be the main script that is called to run all of the others
#The idea is that LTSpice will be open at the same time as the terminal and it is an interactive interface.

import terminal #just do it myself?
import globals as glb

#todo: add an operating system check. Make sure that we are in windows
#call the initialize function?


#This is the main loop of the program. It continues to loop, executing commands, until the exit command.
while(True):
    command = terminal.prompt(" ", glb.DEFAULT_COMMAND) # prompt for the command.
    args = command.split(' ') # split into the command and the parameters to it.
    param = args[1:] # these will be passed as arguments into the various functions
                        # any error checking is done by the various functions. Not here.


    if args[0] in glb.commands : #if the command is in the list. Call the function
        glb.commands[args[0]][glb.FUNCTION_INDEX](param)
    elif command != glb.DEFAULT_COMMAND : # if it doesn't exist then call an error and show the help menu
        print("ERROR: Invalid Command")
        glb.commands['help'][glb.FUNCTION_INDEX]()
