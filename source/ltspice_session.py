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

    def __str__(self):
        toPrint = "LTSpice_Session(" + self.name + ":" + str(self.pid) + ")"
        return toPrint
    def __repr__(self):
        return __str__() #todo: should something else be done here?


## The container class for LTSpice Sessions

class SessionControl() :
    def __init__(self):
        self.sessList = []
        self.EXE_NAME = "XVIIx64.exe"

    '''
    Assumes that toSearch is a list of LTSpice_Sessions. 
    Iterates through them and searches for the pid.
    Returns true if it is found. 
    Returns false otherwise. 
    '''
    def InList(toSearch, pid):
        for i in toSearch:
            if i.GetPID() == pid:
                return True
        return False



    def Kill(pid = None, name = None) :
        if pid != None :
            print(self.sessList)
            for i in self.sessList :
                if i.GetPid() == pid :
                    i.Stop() #stop the process
                    self.sessList.pop(i) #and remove it from the list.
                    break
            print(self.sessList)

    def AddSession(self, sessName, sessPid, isOpen = True):
        self.sessList.append(sessName, sessId, isOpen)

    '''
    Talks with the operating system to determine the pid number of any new ltspice sessions.
    returns  a tuple of 2 lists - one has all of the new pid sessions, the other has all of the removed sessions.
    '''
    def UpdatePids() :
        command = "tasklist"
        output = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #call the command to find all processes
        returned = output.stdout.decode('utf-8') #decode the output
        currentlyRunning = [r for r in returned.split('\n') if self.EXE_NAME in r] #find all of the lines where a session of ltspice is running
        currentPid = [l.split()[1] for l in currentlyRunning] #find the pids of the currently running sessions
        newPid = [p for p in currentPid if not InList(self.sessList, p)] #determine which ones are new.
        for p in newPid : #add them to the previously known
            self.sessList.append(LTSpice_Session("unknown.asc", p, True))
            # print(pidList[-1])
        removedPid = [p for p in self.sessList if p.GetPID() not in currentPid] #find all of the ones that have been stopped
        for p in removedPid : #and removed them from the master list.
            self.sessList.remove(p)
        print("new", newPid)
        print("gone",removedPid)
        print("all", self.sessList)
        return (newPid, removedPid)
