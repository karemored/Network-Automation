import sys
import re

SUCCESS = 1
FAIL = 0

def execComnd(cmd,logs,process):
        process.stdin.write(cmd)
        process.stdin.write("\n")
        printOP(logs,process)

def printOP(logs,process):
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
                                break
                        if re.search('R\w\(config\)#',buffertrack):
                                buffertrack = ""
                                break
                        if re.search('R\w\(config-if\)#',buffertrack):
                                buffertrack = ""
                                break

        return

