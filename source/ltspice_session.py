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
import ltspice_addon_setup as setup
import sys

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

    def Show(self):
        print("File Name : PID")
        print("----------------")
        for i in self.sessList :
            print(i[1], ":", i[2])


    def Kill(self, pid = None, name = None) :
        if pid != None :
            for i in self.sessList :
                if i[2] == int(pid) :
                    print("Closing", i[1])
                    i[0].kill()
                    self.sessList.remove(i)
                    #i.Stop() #stop the process
                    #self.sessList.pop(i) #and remove it from the list.
                    break
        if name != None :
            for i in self.sessList :
                if i[1] == name :
                    print("Closing", i[1])
                    i[0].kill()
                    self.sessList.remove(i)
                    #i.Stop() #stop the process
                    #self.sessList.pop(i) #and remove it from the list.
                    break


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
