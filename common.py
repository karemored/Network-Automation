import sys
import re

import glbvar as glb

SUCCESS = 1
FAIL = 0

###################################################################
# NAME         : execComnd
# DESCRIPTION  : Execute Command on router through the stdin PIPE 
#                of the popen object
# INPUT PARAMS : cmd - command to be executed
#                logs - pointer to the log file
#                process - popen object 
# RETURN       : SUCCESS/FAIL
###################################################################

def execComnd(cmd,logs,process):
        process.stdin.write(cmd)
        process.stdin.write("\n")
        
	return printOP(logs,process)

###################################################################
# NAME         : execComnd
# DESCRIPTION  : Prints the output of the command executed by
#		 execComnd function
# INPUT PARAMS : logs - pointer to the log file
#                process - popen object
# RETURN       : SUCCESS/FAIL
###################################################################

def printOP(logs,process):
	global PING_STAT
	global PRIV_EXECM
	global GLOBAL_EXECM
	global INTF_CONFM
	global ROUTER_CONFM
        
	buffertrack = ""

        while True:
                opparser = process.stdout.read(1)
                if opparser == '':
                        break
                if opparser != '':
                        buffertrack = buffertrack + str(opparser)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()
                        if re.search('R\w#',buffertrack):
                                buffertrack = ""
				opparser = None
				glb.PRIV_EXECM = 1
                                break
                        if re.search('R\w\(config\)#',buffertrack):
                                buffertrack = ""
				opparser = None
				glb.GLOBAL_EXECM = 1
                                break
                        if re.search('R\w\(config-if\)#',buffertrack):
                                buffertrack = ""
				opparser = None
				glb.INTF_CONFM = 1
                                break
			if re.search('R\w\(config-router\)#',buffertrack):
                                buffertrack = ""
                                opparser = None
				glb.ROUTER_CONFM = 1
                                break
			if re.search('Success\srate\sis\s\d+\spercent\s\(\w',buffertrack):
				buffertrack = ""
				if opparser == '0':
					glb.PING_STAT = 0
				else:
					glb.PING_STAT = 1

        return SUCCESS

###################################################################
# NAME         : valIntStatusWr
# DESCRIPTION  : validates the status of interface
# INPUT PARAMS : slot - slot on the router
#		 port - port on the router
#                logs - pointer to the log file
#                process - popen object
# RETURN       : SUCCESS/FAIL
###################################################################

def valIntStatusWr(logs,process,slot,port):
	buffertrack = ""
	params = ""
	
	to_search = "FastEthernet"+str(slot)+"/"+str(port)+"\s+"
	to_search = to_search + "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|unassigned)"
	to_search = to_search + "\s+YES\s+\w+\s+(up|down|administratively down)\s+(\w+)\s+"
	process.stdin.write("show ip interface brief")
	process.stdin.write("\n")
	
	while True:
		opparser = process.stdout.read(1)
		buffertrack = buffertrack + str(opparser)
		
		if re.search(to_search,buffertrack):
			params = buffertrack

		if re.search('R\w#',buffertrack):
			break
	
	search_1 = re.findall(to_search,params)
	
	return search_1[0]

###################################################################
# NAME         : validateRIPWr
# DESCRIPTION  : validates whether RIP is configured or not
# INPUT PARAMS : logs - pointer to the log file
#                process - popen object
# RETURN       : SUCCESS/FAIL
###################################################################

def validateRIPWr(logs,process):
	buffertrack = ""
	SET = 0
	
	process.stdin.write("show ip protocols")
	process.stdin.write("\n")

	while True:
		opparser = process.stdout.read(1)
		buffertrack = buffertrack + str(opparser)
		
		if re.search('Routing Protocol is \"rip\"',buffertrack):
			SET = 1
		if re.search('R\w#',buffertrack):
			break

	return SET		
