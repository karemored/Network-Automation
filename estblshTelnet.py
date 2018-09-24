import pdb
import privMode as mode
import common as cmn

import subprocess as sp
import sys
import re

FAIL = 0
SUCCESS = 1

###################################################################
# NAME         : estbProcess
# DESCRIPTION  : Executes the telnet command on the shell using
#		 popen class of the subprocess module
# INPUT PARAMS : 1. ip : IP of the router to be telnetted
#                2. logs : pointer to the log file
# RETURN       : process object for one telnet session
###################################################################

def estbProcess(logs,ip):
        hostname = ip
        string = ""

        print "...STARTING TELNET SESSION TO " + hostname + "..."
        try:
                process = sp.Popen(['telnet',hostname], stdout = sp.PIPE, stdin = sp.PIPE)
        except:
                print "ERROR : TELNET COMMAND EXECUTION FAILED"
                return None

        return process

###################################################################
# NAME         : estbTelnet
# DESCRIPTION  : Establishes telnet to the router specified in the
#		 process object by providing the username and 
#		 password
# INPUT PARAMS : 1. process object associated with each telnet
#		    session
#                2. pointer to the log file
# RETURN       : SUCCESS
###################################################################

def estbTelnet(logs,process):
        buffertrack = ""

        while True:                      
                opparser = process.stdout.read(1)                        # reads from processs' stdout buffer 
                if opparser == '' and process.poll() == 0:               # check if the buffer is empty or process has terminated
                        break
                if opparser != '':                                       # if reading buffer not completed
                        logs.write(opparser)
                        sys.stdout.write(opparser)                       # log the output of process on console
                        sys.stdout.flush()
                        buffertrack = buffertrack + str(opparser)        # add the characters of the stdout in a string
                        #print buffertrack
                        if re.search(r'Username:\s' , buffertrack):      # regular expression to search for 'USERNAME'
                                #print "Username found"
                                process.stdin.write("u1\n")
                                buffertrack = ""
                        if re.search(r'Password:\s' , buffertrack):      # regular expression to search for 'PASSWORD'
                                #print "passwd found"
                                process.stdin.write("admin\n")
                                buffertrack = ""
                                break
        return SUCCESS

def genSession():
        gsessionid = gsessionid + 1;

###################################################################
# NAME         : setLogFile
# DESCRIPTION  : sets up log file for all logging 
# INPUT PARAMS : none
# RETURN       : pointer to file containing logs
###################################################################

def setLogFile():
        print "...ALL THE LOGS WILL BE STORED IN THE \"log.txt\" FILE..."
        print "...LOGS CAN BE USED TO CHECK ALL THE CONFIGURARIONS..."
        print "...COMMANDS ON THE ROUTER..."

        filename = "log.txt"
        logs = open(filename,"w")
        return logs

###################################################################
# NAME         : fetchIP
# DESCRIPTION  : appends to a list of all IPs of the routers to be 
#		 telnetted
# INPUT PARAMS : none
# RETURN       : list of IPs of the routers to be telnetted
###################################################################

def fetchIP():
        list_ip = []                                                     # list to store the IPs of all the routers
        list_ip.append("192.168.80.10") 
        list_ip.append("192.168.80.20")
        list_ip.append("192.168.80.30")

        return list_ip                                                   # return list of IPs to the main function 
 
###################################################################
# NAME         : main
# DESCRIPTION  : main function execution to start fro  this point
# INPUT PARAMS : none
# RETURN       : none 	
###################################################################

def main():
        #genSession()
        sessionID = 1                                                    # defining session ID to each telnet session   
        session_list = ['zero']                                          # list to maintain all elnet sessions   
        logs = setLogFile()                                              # log file to log all commands as they appear on 
                                               				 # a router
        list_ip = fetchIP()
        for ip in list_ip:
                session_list.append( estbProcess(logs,ip) )              # establish telnet session and store it in session list 
                if session_list[sessionID] != None :
                        if estbTelnet(logs,session_list[sessionID]):
                                print "...TELNET ACCESS TO ROUTER SUCCESSFUL..."
                else:
                        print "ERROR : PROCESS ESTABLISH FAIL"

                sessionID = sessionID + 1
        if mode.jumpToMode(logs,session_list) is FAIL :                  # jump to User Executive mode 
		print "ERROR : Failed to enter UserExec/ PrivExec Mode
if __name__ ==  "__main__" :
        main()

