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
# NAME         : confEIGRP
# DESCRIPTION  : Configure EIGRP on the router
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
#                3. as_num : AS number
#		 4. ip address to be given to the network command
#                5. wildcard- wildcard mask 
# RETURN       : SUCCESS/FAIL
###################################################################

def confEIGRP(logs,process,as_num,ip,wildcard):
        router_eigrp = "router eigrp "
        router_eigrp.append(str(as_num))
        network = "network "
        glb.initRouterConf()
        if cmn.execComnd(router_eigrp,logs,process) is FAIL:
                return FAIL

        if glb.valRouterConf() is FAIL:
                print "ERROR : FAILED TO ENTER ROUTER CONF MODE"
                return FAIL

        network = network + ip + " " + wildcard
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
# NAME         : enableEIGRP
# DESCRIPTION  : Function to enter into EIGRP configuration
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def enableEIGRP(logs,process,as_num,ip,wildcard):
        if glb.valPrivExec() is FAIL:
                print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
                print "ERROR : FUNCTION : \"enableEIGRP\" returning failure"
                return FAIL

        if globalConfMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"

        if confEIGRP(logs,process,as_num,ip,wildcard) is FAIL:
                print "ERROR : FUNCTION \'confEIGRP\' returned Failure"

        if extGlobalMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'extGlobalMode\' returned Failure"

###################################################################
# NAME         : validateEIGRP
# DESCRIPTION  : Validate EIGRP config
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def validateEIGRP(logs,process):
        if cmn.validateEIGRPWr(logs,process) == 0:
                print "EIGRP CONFIG FAIL"
        else:
                print "EIGRP CONFIG SUCCESSFUL"


