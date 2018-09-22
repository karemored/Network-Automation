import showConfigs as shwc
import interface_config as intconf
import connectivity as png

SUCCESS = 1
FAIL = 0

#...INSIDE PRIVILEDGE EXECUTIVE WRAPPER...
#...THIS FUNCTION WILL BE THE CONTROL CENTER...
#...EVERY CONFIGURATION SHOULD RETURN CONTROL TO THIS FUNCTION...

def privExecModeWr(logs,session_list):
        buffertrack = ""
        cmd_to_exec = ""
        list_show = []

        if shwc.showConfigs(logs,session_list[1]) is FAIL:
                return FAIL

        if shwc.showConfigs(logs,session_list[2]) is FAIL:
                return FAIL

        if shwc.showConfigs(logs,session_list[3]) is FAIL:
                return FAIL

        intconf.intfConfigs(logs,session_list[1],1,0,"20.0.0.1","255.255.255.0")
        intconf.intfConfigs(logs,session_list[1],2,0,"30.0.0.1","255.255.255.0")
        intconf.intfConfigs(logs,session_list[2],1,0,"20.0.0.2","255.255.255.0")
        intconf.intfConfigs(logs,session_list[2],2,0,"30.0.0.1","255.255.255.0")
        intconf.intfConfigs(logs,session_list[3],2,0,"30.0.0.2","255.255.255.0")

        if shwc.showConfigs(logs,session_list[1]) is FAIL:
                return FAIL

        if shwc.showConfigs(logs,session_list[2]) is FAIL:
                return FAIL

        if shwc.showConfigs(logs,session_list[3]) is FAIL:
                return FAIL
        
	png.chkPing(logs,session_list[1],"20.0.0.2")


        return SUCCESS


