# Created December 11, 2018 by Wesley Stirk
# Last updated December 12, 2018 by Wesley Stirk
"""
This file is to have all of the functions that will be called by the ltspice_terminal.
This is where the bulk of the functionality will be added to the program.

IMPORTANT: All functions that are to be called by the ltspice_terminal at least need to have one argument for the parameters list.
This is because how it it called in ltspice_terminal. If uneeded, just put it as a default parameter =None
"""

import globals as glb

##

# displays the help menu
# needs no parameters and returns no values
def terminal_help(params=None):
    for com in glb.commands.keys() : # print all of the helps
        print(com, ": ", glb.commands[com][glb.HELP_INDEX])

