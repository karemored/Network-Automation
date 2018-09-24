
import pdb
import privMode as mode
import common as cmn

import subprocess as sp
import sys
import re

FAIL = 0
SUCCESS = 1

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


def estbTelnet(logs,process):
        buffertrack = ""

        while True:
                opparser = process.stdout.read(1)
                if opparser == '' and process.poll() == 0:
                        break
                if opparser != '':
                        logs.write(opparser)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()
                        buffertrack = buffertrack + str(opparser)
                        #print buffertrack
                        if re.search(r'Username:\s' , buffertrack):
                                #print "Username found"
                                process.stdin.write("u1\n")
                                buffertrack = ""
                        if re.search(r'Password:\s' , buffertrack):
                                #print "passwd found"
                                process.stdin.write("admin\n")
                                buffertrack = ""
                                break
        return SUCCESS

def genSession():
        gsessionid = gsessionid + 1;

def setLogFile():
        print "...ALL THE LOGS WILL BE STORED IN THE \"log.txt\" FILE..."
        print "...LOGS CAN BE USED TO CHECK ALL THE CONFIGURARIONS..."
        print "...COMMANDS ON THE ROUTER..."

        filename = "log.txt"
        logs = open(filename,"w")
        return logs

def fetchIP():
        list_ip = []
        list_ip.append("192.168.80.10")
        list_ip.append("192.168.80.20")
        list_ip.append("192.168.80.30")

        return list_ip

def main():
        #genSession()
        sessionID = 1
        session_list = ['zero']
        logs = setLogFile()

        list_ip = fetchIP()
        for ip in list_ip:
                session_list.append( estbProcess(logs,ip) )
                if session_list[sessionID] != None :
                        if estbTelnet(logs,session_list[sessionID]):
                                print "...TELNET ACCESS TO ROUTER SUCCESSFUL..."
                else:
                        print "ERROR : PROCESS ESTABLISH FAIL"

                sessionID = sessionID + 1

        mode.jumpToMode(logs,session_list)

if __name__ ==  "__main__" :
        main()

