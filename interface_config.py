import  common as cmn
import glbvar as glb

FAIL = 0
SUCCESS = 1

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
		print "ERROR : FAILED TO ENETER GLOBAL EXEC MODE"
		return FAIL
        
	return SUCCESS

###################################################################
# NAME         : intConfMode
# DESCRIPTION  : Enters Interface conf mode
# INPUT PARAMS : 1. process : a telnet session
#		 2. Slot to be configured
#	         3. port to be configured
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def intConfMode(logs,process,slot,port):
	glb.initInfConf()
        cmd = ""
        list_cmd = ['interface fastethernet ']
        list_cmd.append(str(slot))
        list_cmd.append("/")
        list_cmd.append(str(port))
        cmd = ''.join(list_cmd)

        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

	if glb.valInfConf is FAIL:
		"ERROR : FAILED TO ENTER INTERFACE CONF MODE"
		return FAIL

        return SUCCESS

###################################################################
# NAME         : confIPAddress
# DESCRIPTION  : Assigns IP address to a port
# INPUT PARAMS : 1. process : a telnet session
#                2. ip : ip address to be configured
#                3. mask : mask to be cofigured
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def confIPAddress(logs,process,ip,mask):
        cmd = "ip address " + ip + " " + mask + " "
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        cmd = "no shutdown "
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        return SUCCESS

###################################################################
# NAME         : extGlobalMode
# DESCRIPTION  : Exits to Priv exec mode
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
# NAME         : intfConfigs
# DESCRIPTION  : Entry point to the Global Conf mode
#		 from PrivExec mode
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
#		 3. slot : slot to be configured
#		 4. port : port to be configured
# RETURN       : SUCCESS/FAIL
###################################################################

def intfConfigs(logs,process,slot,port,ip,mask):
	if glb.valPrivExec() is FAIL:
		print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
		print "ERROR : FUNCTION : \"intfConfigs\" returning failure"
		return FAIL

        if globalConfMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"

        if intConfMode(logs,process,slot,port) is FAIL:
                print "ERROR : FUNCTION \'intConfMode\' returned Failure"

        if confIPAddress(logs,process,ip,mask) is FAIL:
                print "ERROR : FUNCTION \'confIPAddress\' returned Failure"

        if extGlobalMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'extGlobalMode\' returned Failure"

