import ltspice_commands
import testtest

commands = {
    'exit': exit,
    'test': testtest.test,
    'help': ltspice_commands.terminal_help
}

helpInfo = {
    'exit': 'exit the ltspice_terminal',
    'test': "perform a basic test",
    'help': "display this help menu"
}