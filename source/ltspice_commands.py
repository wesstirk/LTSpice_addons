# Created December 11, 2018 by Wesley Stirk
# Last updated December 24, 2018 by Wesley Stirk
"""
This file is to have all of the functions that will be called by the ltspice_terminal.
This is where the bulk of the functionality will be added to the program.

IMPORTANT: All functions that are to be called by the ltspice_terminal at least need to have one argument for the parameters list.
This is because how it it called in ltspice_terminal. If uneeded, just put it as a default parameter =None
"""

import globals as glb
import ltspice_addon_setup as setup
import os
import sys

##

# displays the help menu
# needs no parameters and returns no values
def terminal_help(params=None):
    for com in glb.commands.keys() : # print all of the helps
        print(com, ": ", glb.commands[com][glb.HELP_INDEX])


"""
Starts LTSpice.
The EXE_FILE parameter in the cfg file must point to the actual LTSpice program in order for this function to work properly
The params are not used. 
returns True if it worked False otherwise
"""
def start_ltspice(params=None) :
    print("opening LTSpice...")
    try:
        cfg = setup.read_cfg()
        BAT_NAME = "ltspice_start.bat"

        #it's a bit of a hack, but it's easiest to work from a bat file while in windows. It's easier to start a subprocess on my machine.
        batFile = open(BAT_NAME, 'w') #create the bat file
        command = 'start "LTSpice with Terminal" ' + cfg['EXE_FILE']  #this is the command. Start, then the title, then what is being started
        batFile.write(command) #write the command to the file
        batFile.close() #close the file so that it can be used

        os.system(BAT_NAME) #run the bat file

        return True
    except:
        print("Error in opening LTSpice")
        print(sys.exc_info()[0], " has occurred.")
        return False

def tolerances(params=None) :
    print("tolerances")
