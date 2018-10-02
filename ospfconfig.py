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
# NAME         : confOSPF
# DESCRIPTION  : Configure OSPF on the router
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
#		 3. ip address to be given to the network command
#                4. wildcard- wildcard mask 
# RETURN       : SUCCESS/FAIL
###################################################################

def confOSPF(logs,process,ip,wildcard):
        network = "network "
        glb.initRouterConf()
        if cmn.execComnd("router ospf 1",logs,process) is FAIL:
                return FAIL

        if glb.valRouterConf() is FAIL:
                print "ERROR : FAILED TO ENTER ROUTER CONF MODE"
                return FAIL

        network = network + ip + " " + wildcard + " area 0"
        if cmn.execComnd(network,logs,process) is FAIL:
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
# NAME         : enableOSPF
# DESCRIPTION  : Function to enter into OSPF configuration
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def enableOSPF(logs,process,ip,wildcard):
        if glb.valPrivExec() is FAIL:
                print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
                print "ERROR : FUNCTION : \"enableOSPF\" returning failure"
                return FAIL

        if globalConfMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"

        if confOSPF(logs,process,ip,wildcard) is FAIL:
                print "ERROR : FUNCTION \'confOSPF\' returned Failure"

        if extGlobalMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'extGlobalMode\' returned Failure"

###################################################################
# NAME         : validateOSPF
# DESCRIPTION  : Validate OSPF config
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def validateOSPF(logs,process):
        if cmn.validateOSPFWr(logs,process) == 0:
                print "OSPF CONFIG FAIL"
        else:
                print "OSPF CONFIG SUCCESSFUL"


