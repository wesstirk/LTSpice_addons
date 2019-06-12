#Created December 11, 2018 by Wesley Stirk
#Last updated June 11, 2019 by Wesley Stirk
"""
This file is for all global constants and information that is needed for the entire program.
"""

import ltspice_commands as comms
import testtest

## constants

FUNCTION_INDEX = 0 #index of the tuple that contains the function pointer.
HELP_INDEX = 1 #index of the help description

DEFAULT_COMMAND = " "


# Feel free to add more commands and funtionality to the terminal. This will typically be done by adding more commands.
# This terminal was designed to be easily modified for your purposes.
# command syntax :
# 'command_name': (<function_pointer>, 'help description')

commands = {
    'exit': (exit, 'exit the ltspice_terminal'),
    'test': (testtest.test, "perform a basic test"),
    'help': (comms.terminal_help, "display this help menu"),
    'start': (comms.start_ltspice, 'starts the LTspice program\n \tMust be properly configured in the cfg file.'),
    'setup': (comms.ltsetup, 'configures needed files for use in the system.\n \tShould only need to be used once.')
}

