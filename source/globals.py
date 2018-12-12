import ltspice_commands
import testtest

## constants

FUNCTION_INDEX = 0
HELP_INDEX = 1

DEFAULT_COMMAND = " "


# Feel free to add more commands and funtionality to the terminal. This will typically be done by adding more commands.
# This terminal was designed to be easily modified for your purposes.
# command syntax :
# 'command_name': (<function_pointer>, 'help description')

commands = {
    'exit': (exit, 'exit the ltspice_terminal'),
    'test': (testtest.test, "perform a basic test"),
    'help': (ltspice_commands.terminal_help, "display this help menu")
}

