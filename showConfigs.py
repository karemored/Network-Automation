import common as cmn
import glbvar as glb

FAIL = 0
SUCCESS = 1

###################################################################
# NAME         : genCommand
# DESCRIPTION  : compltes the show command using the parameters
# INPUT PARAMS : 1. params_list : list of params
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def genCommand(logs,param_list):
        cmd = ""
        list_show = ["show "]

	for itr in range (0,len(param_list)):
		list_show.append(param_list[itr])

        cmd = ''.join(list_show)

        return cmd

###################################################################
# NAME         : showIpIntConfigs
# DESCRIPTION  : provides the params to form the complete command
#                calls function:"execComnd" to execute command
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def showIpIntConfigs(logs,process):
        if glb.valPrivExec() is FAIL:
                print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
                print "ERROR : FUNCTION : \"showIpIntConfigs\" returning failure"
                return FAIL
	
	param_list = "ip interface brief"
        cmd = genCommand(logs,param_list)
		
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        return SUCCESS
