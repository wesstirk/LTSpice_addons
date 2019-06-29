#created June 11, 2019 by Wesley Stirk
#last updated June 11, 2019 by Wesley Stirk

'''
This file contains a class for managing the LTSpice sessions.
Used to keep track of all of the needed data when opening and closing various files.
'''

import math
import os
import subprocess
import signal
import ltspice_addon_setup as setup
import sys

## The container class for LTSpice Sessions

OBJ_INDEX = 0
NAME_INDEX = 1
PID_INDEX = 2

class SessionControl() :
    def __init__(self):
        self.sessList = [] #a list that will keep track of the tuples of session information
        self.EXE_NAME = setup.read_cfg()['EXE_FILE'] # the executable file to call
        self.startNum = 0 #used to keep track of the sessions that don't have file names at the start.
    """
    Starts LTSpice.
    The EXE_FILE parameter in the cfg file must point to the actual LTSpice program in order for this function to work properly
    The params are not used. 
    returns True if it worked False otherwise
    """

    def Start(self):
        print("opening LTSpice...")
        try:
            print(self.EXE_NAME)
            newSess = subprocess.Popen(self.EXE_NAME)
            if newSess.poll() == None or newSess.returncode == 0: #if it is still open and it worked.
                self.sessList.append((newSess, "nofile{}".format(self.startNum), newSess.pid) )
                self.startNum += 1
            # os.system(command)
            return True
        except Exception as err:
            print("Error in opening LTSpice")
            print(err)
            return False

    '''
    Starts LTSpice with a specified file opened
    params must have one value - the file to be opened
    returns True if it worked, False otherwise
    '''

    def OpenFile(self, file):
        try:
            print("Opening", file, "now...")
            print(self.EXE_NAME)
            newSess = subprocess.Popen(self.EXE_NAME+" "+file)
            ##todo: try and make it so it doesn't get added to the list if it is an invalid file....
            if newSess.poll() == None or newSess.returncode == 0: #if it is still open and it worked.
                self.sessList.append((newSess, file, newSess.pid))
            # os.system(command)
            return True
        except Exception as err:
            print("Error in opening LTSpice")
            print(err)
            return False

    def Show(self):
        print("File Name : PID")
        print("----------------")
        for i in self.sessList :
            print(i[NAME_INDEX], ":", i[PID_INDEX])


    def Kill(self, pid = None, name = None) :
        if pid != None :
            for i in self.sessList :
                if i[PID_INDEX] == int(pid) :
                    print("Closing", i[NAME_INDEX])
                    i[OBJ_INDEX].kill()
                    self.sessList.remove(i)
                    #i.Stop() #stop the process
                    #self.sessList.pop(i) #and remove it from the list.
                    break
        if name != None :
            for i in self.sessList :
                if i[NAME_INDEX] == name :
                    print("Closing", i[NAME_INDEX])
                    i[OBJ_INDEX].kill()
                    self.sessList.remove(i)
                    #i.Stop() #stop the process
                    #self.sessList.pop(i) #and remove it from the list.
                    break