#created June 11, 2019 by Wesley Stirk
#last updated June 11, 2019 by Wesley Stirk

'''
This file contains the LTSpice session class.
Used to keep track of all of the needed data when opening and closing various files.
'''

import math
import os
import subprocess
import signal

class LTSpice_Session:
    def __init__(self, name="dummy.asc", pid=math.nan, isOpen=False):
        self.name = name #the name of the file
        self.pid = pid #the pid reference in the operating system (mainly used for closing the program when needed."
        self.isOpen = isOpen #keeping track of whether the session of ltspice has actually been opened.
    def SetName(self, newName):
        self.name = newName
    def GetName(self):
        return self.name
    def SetPID(self,newPid):
        self.pid = newPid
    def GetPID(self):
        return self.pid
    def SetOpen(self, open=True):
        self.isOpen = open
    def SetClosed(self):
        self.isOpen = False
    def GetOpenStatus(self):
        return self.isOpen
    def SetVars(self, name="dummy.asc", pid=math.nan, isOpen=False):
        self.name = name  # the name of the file
        self.pid = pid  # the pid reference in the operating system (mainly used for closing the program when needed."
        self.isOpen = isOpen  # keeping track of whether the session of ltspice has actually been opened.

    def Stop(self):
        os.kill(int(self.pid), signal.SIGINT)
## the support functions for the sessions

pidList = [] #the list that keeps track of all of the active ltspice sessions

EXE_NAME = "XVIIx64.exe"

'''
Talks with the operating system to determine the pid number of any new ltspice sessions. 
returns 2 lists - one has all of the new pid sessions, the other has all of the removed sessions. 
'''
def UpdatePids() :
    command = "tasklist"
    global pidList
    output = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #call the command to find all processes
    returned = output.stdout.decode('utf-8') #decode the output
    currentlyRunning = [r for r in returned.split('\n') if EXE_NAME in r] #find all of the lines where a session of ltspice is running
    currentPid = [l.split()[1] for l in currentlyRunning] #find the pids of the currently running sessions
    newPid = [p for p in currentPid if p not in pidList] #determine which ones are new.
    for p in newPid : #add them to the previously known
        pidList.append(p)
    removedPid = [p for p in pidList if p not in currentPid] #find all of the ones that have been stopped
    for p in removedPid : #and removed them from the master list.
        pidList.remove(p)
    print("new", newPid)
    print("gone",removedPid)
    print("all", pidList)
    return newPid, removedPid
