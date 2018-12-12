import os

CFG_FILE = 'ltspice_addon.cfg' #currently needs to be in the same directory.

"""
reads the cfg file with all of the variables that need to be saved through future use of the program
returns a dictionary with all of the variables in the cfg files
"""
def read_cfg() :
    f = open(CFG_FILE, 'r');
    vals = {} #make it a dictionary for easy access
    #todo: add the ability to have comments / header in cfg file
    for line in f :
        info = line.split(';') #all values must be separated by a semicolon
        vals[info[0]] = info[1] #the first term will always be the variable name.
                                #the second term will be the variable value
    return vals


def find_exe() :
    print("find exe")