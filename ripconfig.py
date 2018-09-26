###################################################################
# NAME         : globalConfMode
# DESCRIPTION  : Enters the global conf mode
# INPUT PARAMS : 1. process : a telnet session
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def globalConfMode(logs,process):
        if cmn.execComnd("configure terminal",logs,process) is FAIL:
                return FAIL

        return SUCCESS

def confRIP


def enableRIP(logs,session_id,ip):
	if globalConfMode(logs,session_id) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"
