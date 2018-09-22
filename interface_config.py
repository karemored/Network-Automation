import  common as cmn

FAIL = 0
SUCCESS = 1

def globalConfMode(logs,process):
        if cmn.execComnd("configure terminal",logs,process) is FAIL:
                return FAIL

        return SUCCESS

def intConfMode(logs,process,slot,port):
        cmd = ""
        list_cmd = ['interface fastethernet ']
        list_cmd.append(str(slot))
        list_cmd.append("/")
        list_cmd.append(str(port))
        cmd = ''.join(list_cmd)

        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        return SUCCESS

def confIPAddress(logs,process,ip,mask):
        cmd = "ip address " + ip + " " + mask + " "
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        cmd = "no shutdown "
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL

        return SUCCESS

def extGlobalMode(logs,process):
        if cmn.execComnd("exit",logs,process) is FAIL:
                return FAIL

        if cmn.execComnd("exit",logs,process) is FAIL:
                return FAIL

        return SUCCESS

def intfConfigs(logs,process,slot,port,ip,mask):
        if globalConfMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'globalConfMode\' returned Failure"

        if intConfMode(logs,process,slot,port) is FAIL:
                print "ERROR : FUNCTION \'intConfMode\' returned Failure"

        if confIPAddress(logs,process,ip,mask) is FAIL:
                print "ERROR : FUNCTION \'confIPAddress\' returned Failure"

        if extGlobalMode(logs,process) is FAIL:
                print "ERROR : FUNCTION \'extGlobalMode\' returned Failure"

