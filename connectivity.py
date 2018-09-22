import sys
import re
import common as cmn

SUCCESS = 1
FAIL = 0

def chkPing(logs,process,ip):
	cmd = "ping "+ip
	
	if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

	
