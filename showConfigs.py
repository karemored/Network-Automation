import common as cmn

FAIL = 0
SUCCESS = 1

def genCommand():
        #print "...inside gencommands..."
        cmd = ""

        list_show = ["show "]
        list_show.append("ip interface brief")

        cmd = ''.join(list_show)

        return cmd

def showConfigs(logs,process):
        #print "...inside showConfigs..."
        cmd = genCommand()
        #print "cmd:" + cmd
        if cmn.execComnd(cmd,logs,process) is FAIL:
                return FAIL
        #print "first cmd success"
        #cmn.printOP(logs,process)

        #print "show config success"
        return SUCCESS

