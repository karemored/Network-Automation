import genScript as script
import glbvar as glb
import re
import sys

SUCCESS = 1
FAIL = 0

###################################################################
# NAME         : usrExecMode
# DESCRIPTION  : Script enters Userexec mode after successful telnet
#		 login, checks the prompt of the Userexec mode.
#		 Once the Userexec mode is confirmed, "enable"
#		 command is used to enter the PrivExec mode 
# INPUT PARAMS : 1. logs : pointer to the log file
#                2. session_list : list contaiing process
#                   objects (telnet sessions)
# RETURN       : SUCCESS/FAIL
###################################################################

def usrExecMode(logs,session_list):
        buffertrack = ""

        for itr in range(1,len(session_list)):
                process = session_list[itr]                                       # variable process catches each popen object
                while True:
                        opparser = process.stdout.read(1)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()
                        if opparser != '':
                                buffertrack = buffertrack + str(opparser)
                                #process.stdin.write("enable\n")
                                if re.search('R\w>',buffertrack):                # Check weather the Userexec prompt is met
                                        process.stdin.write("enable\n")
                                        buffertrack = ""
                                if re.search('Password:\s',buffertrack):         # enter password for entering PrivExec mode
                                        process.stdin.write("admin\n")
                                        buffertrack = ""
                                if re.search('R\w#',buffertrack):                # if PrivExec prompt met; break out of the loop
                                        buffertrack = ""
                                        break
        return SUCCESS

#####################################################################
# NAME         : privExecMode
# DESCRIPTIO   : Confirms weather the control is at the PrivExec mode
# INPUT PARAMS : 1. logs : pointer to the log file
#                2. session_list : list contaiing process
#                   objects (telnet sessions)
# RETURN       : SUCCESS 	
#####################################################################

def privExecMode(logs,session_list):
	glb.initPrivExec()
        buffertrack = ""

        for itr in range(1,len(session_list)):
                process = session_list[itr]
                process.stdin.write("\n")

                while True:
                        opparser = process.stdout.read(1)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()

                        if opparser != '':
                                buffertrack = buffertrack + str(opparser)

                                if re.search('R\w#',buffertrack):
                                        buffertrack = ""
					glb.PRIV_EXECM = 1
                                        break
	if glb.valPrivExec() is FAIL:
		print "ERROR : FAILED TO ENETER PRIV EXEC MODE"
		return FAIL
        return SUCCESS

###################################################################
# NAME         : junpToMode
# DESCRIPTIO   : Control transferred to this function after
#		 telnet successful
# INPUT PARAMS : 1. logs : pointer to the log file
#		 2. session_list : list contaiing process
#		    objects (telnet sessions)
# RETURN       : FAIL/none 	
###################################################################

def jumpToMode(logs,session_list):
        if usrExecMode(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"userExecMode\" RETURNED FAILURE"
                return FAIL

        if privExecMode(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"privExecMode\" RETURNED FAILURE"
                return FAIL

        if script.privExecModeWr(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"privExecModeWr\" RETURNED FAILURE"
                return FAIL



