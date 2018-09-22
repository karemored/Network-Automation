import genScript as script
import re
import sys

SUCCESS = 1
FAIL = 0

def usrExecMode(logs,session_list):
        buffertrack = ""

        for itr in range(1,len(session_list)):
                process = session_list[itr]
                while True:
                        opparser = process.stdout.read(1)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()
                        if opparser != '':
                                buffertrack = buffertrack + str(opparser)
                                #process.stdin.write("enable\n")
                                if re.search('R\w>',buffertrack):
                                        process.stdin.write("enable\n")
                                        buffertrack = ""
                                if re.search('Password:\s',buffertrack):
                                        process.stdin.write("admin\n")
                                        buffertrack = ""
                                if re.search('R\w#',buffertrack):
                                        buffertrack = ""
                                        #print "\n...INTO PRIVILEGE EXEC MODE..$
                                        #print "...PASSING CONTROL TO PRIV EXEC$
                                        break
        return SUCCESS

def privExecMode(logs,session_list):
        #show commands to be excuted from imdependednt script
        #interface configs
        #vlan configs
        #route protocols configs
        #lets make priv exec mode as the standby mode
        #all confg scripts would require to get back here(call this finction)

        buffertrack = ""


        for itr in range(1,len(session_list)):
                process = session_list[itr]
                process.stdin.write("\n")

                while True:
                        opparser = process.stdout.read(1)
                        sys.stdout.write(opparser)
                        sys.stdout.flush()

                        if opparser != '':
                                buffertrack = buffertrack + str(opparser)

                                if re.search('R\w#',buffertrack):
                                        #process.stdin.write("\n")
                                        #process.stdin.write("\n")
                                        buffertrack = ""
                                        #if script.privExecModeWr(logs,process):
                                        break
        return SUCCESS

def jumpToMode(logs,session_list):
        if usrExecMode(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"userExecMode\" RETURNED FAILURE"
                return FAIL

        if privExecMode(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"userExecMode\" RETURNED FAILURE"
                return FAIL

        if script.privExecModeWr(logs,session_list) is FAIL:
                print "ERROR : FUNCTION \"userExecMode\" RETURNED FAILURE"
                return FAIL



