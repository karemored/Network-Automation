import time

import glbvar as glb
import common as cmn

SUCCESS = 1
FAIL = 0
###################################################################
# NAME         : globalConfMode
# DESCRIPTION  : Enters the global conf mode
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def globalConfMode(logs,process):
	glb.initGlbExec()
        if cmn.execComnd("configure terminal",logs,process) is FAIL:
                return FAIL

	if glb.valGlbExec() is FAIL:
		print "ERROR : FAILED TO ENTER GLOBAL EXEC MODE"
		return FAIL	
        return SUCCESS

###################################################################
# NAME         : confRIP
# DESCRIPTION  : Configure RIP on the router
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
#                3. ip address to be given to the network command
# RETURN       : SUCCESS/FAIL
###################################################################

def confRIP(logs,process,ip):
	network = "network "
	glb.initRouterConf()
	if cmn.execComnd("router rip",logs,process) is FAIL:
                return FAIL

	if glb.valRouterConf() is FAIL:
		print "ERROR : FAILED TO ENTER ROUTER CONF MODE"
		return FAIL
	
	if cmn.execComnd("version 2",logs,process) is FAIL:
                return FAIL

	network = network + ip 
	if cmn.execComnd(network,logs,process) is FAIL:
                return FAIL

	if cmn.execComnd("no auto-summary",logs,process) is FAIL:
                return FAIL

	return SUCCESS

###################################################################
# NAME         : extGlobalMode
# DESCRIPTION  : Exit Router conf mode and enter Global conf mode
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def extGlobalMode(logs,process):
        if cmn.execComnd("exit",logs,process) is FAIL:
                return FAIL

        if cmn.execComnd("exit",logs,process) is FAIL:
                return FAIL
	
        return SUCCESS

###################################################################
# NAME         : enableRIP
# DESCRIPTION  : Function to enter into RIP configuration
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################
	
def enableRIP(logs,process,ip):
        if glb.valPrivExec() is FAIL:
                print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
                print "ERROR : FUNCTION : \"enableRIP\" returning failure"
                return FAIL

	if globalConfMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"
	
	if confRIP(logs,process,ip) is FAIL:	
		print "ERROR : FUNCTION \'confRIP\' returned Failure"

	if extGlobalMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'extGlobalMode\' returned Failure"

###################################################################
# NAME         : validateRIP
# DESCRIPTION  : Validate RIP config
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def validateRIP(logs,process):	
	if cmn.validateRIPWr(logs,process) == 0:
		print "RIP CONFIG FAIL"
	else:
		print "RIP CONFIG SUCCESSFUL"

		
