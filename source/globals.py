#Created December 11, 2018 by Wesley Stirk
#Last updated June 11, 2019 by Wesley Stirk
"""
This file is for all global constants and information that is needed for the entire program.
"""

import ltspice_commands as comms
import testtest
import ltspice_session

## constants

FUNCTION_INDEX = 0 #index of the tuple that contains the function pointer.
HELP_INDEX = 1 #index of the help description

DEFAULT_COMMAND = " "


##global variables used among many parts of the program

currentFile = ltspice_session.LTSpice_Session() #this will be used later on and will be set and used by other functions.
    #uses the default constructor for now.

# Feel free to add more commands and funtionality to the terminal. This will typically be done by adding more commands.
# This terminal was designed to be easily modified for your purposes.
# command syntax :
# 'command_name': (<function_pointer>, 'help description')

commands = {
    'exit': (exit, 'exit the ltspice_terminal'),
    'test': (testtest.test, "perform a basic test"),
    'help': (comms.terminal_help, "display this help menu"),
    'start': (comms.start_ltspice, 'starts the LTspice program\n \tMust be properly configured in the cfg file.'),
    'setup': (comms.ltsetup, 'configures needed files for use in the system.\n \tShould only need to be used once.'),
    'test2': (testtest.test2, "perfomr a helper test"),
    'open': (comms.open_ltspice_file, 'opens the specified asc file in LTSpice'),
    'close': (comms.close_ltspice, 'closes ltspice (not the terminal)'),
    'ls': (comms.sys_ls, 'shows the files in the current directory, (like the ls command in linux)'),
    'cd': (comms.sys_cd, 'moves to a different direcoty'),
    'pwd': (comms.sys_pwd, 'shows the current directory path')
}

