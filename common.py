import sys
import re

import glbvar as glb

SUCCESS = 1
FAIL = 0

def execComnd(cmd,logs,process):
        process.stdin.write(cmd)
        process.stdin.write("\n")
        
	return printOP(logs,process)

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


def valIntStatusWr(logs,process,slot,port):
	buffertrack = ""
	
	to_search = "FastEthernet"+str(slot)+"/"+str(port)+"\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES\s+\w+\s+(\w+)\s+(\w+)\s+"
	process.stdin.write("show ip interface brief")
	process.stdin.write("\n")
	
	while True:
		opparser = process.stdout.read(1)
		buffertrack = buffertrack + str(opparser)
		
		if re.search(to_search,buffertrack):
			
			break
	
	search_1 = re.findall(to_search,buffertrack)
	
	return search_1[0]
