# Created December 11, 2018 by Wesley Stirk
# Last updated June 11, 2018 by Wesley Stirk
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
import subprocess
import ltspice_session as sess

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
    glb.activeFiles.Start()

def tolerances(params=None) :
    print("tolerances")

def ltsetup(params=None) :
    print('setup time')
    setup.find_exe()

def sys_ls(params=None) :
    files = os.listdir()
    for f in files :
        print(f)

def sys_cd(params=None) :
    path = params[0]
    os.chdir(path)

def sys_pwd(params=None) :
    print(os.path.abspath(os.curdir))

'''
Starts LTSpice with a specified file opened
params must have one value - the file to be opened
returns True if it worked, False otherwise
'''
def open_ltspice_file(params=None) :
    if len(params) < 1 :
        print("Error in opening the LTSpice file")
        print("No file provided!")
        return False
    glb.activeFiles.OpenFile(params[0])

def show_sessions(params=None) :
    glb.activeFiles.Show()

def close_ltspice(params=None) :
    if len(params) < 1 :
        print("Error in closing the LTSpice session")
        print("No arguments provided!")
        return False

    if params[0].isnumeric() :
        glb.activeFiles.Kill(pid=params[0])
    else :
        glb.activeFiles.Kill(name=params[0])