import sys
import re

import common as cmn
import glbvar as glb

SUCCESS = 1
FAIL = 0

global PING_STAT

def chkPing(logs,process,ip):
	if glb.valPrivExec() is FAIL:
                print "ERROR : CONTROL NOT AT PRIVEXEC MODE"
                print "ERROR : FUNCTION : \"chkPing\" returning failure"
                return FAIL

	glb.initPingStat()
	cmd = "ping "+ip
	
	if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL
	
	if glb.PING_STAT == 0:
		return FAIL
	else:
		return SUCCESS
	
