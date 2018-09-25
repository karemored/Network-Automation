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
                                break
                        if re.search('R\w\(config\)#',buffertrack):
                                buffertrack = ""
				opparser = None
                                break
                        if re.search('R\w\(config-if\)#',buffertrack):
                                buffertrack = ""
				opparser = None
                                break
			if re.search('Success\srate\sis\s\d+\spercent\s\(\w',buffertrack):
				buffertrack = ""
				if opparser == '0':
					glb.PING_STAT = 0
				else:
					glb.PING_STAT = 1

        return SUCCESS
