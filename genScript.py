import showConfigs as shwc
import interface_config as intconf
import connectivity as png

SUCCESS = 1
FAIL = 0

###################################################################
# NAME         : privExecModeWr
# DESCRIPTION  : Wrapper for Priviledge Exec Mode
#		 Functions with appropriate confis are called 
#		 from this function
#		 Every config function after execution must 
#		 return control to this wrapper function
# INPUT PARAMS : 1. session_list : list of telnet sessions
#                2. logs : pointer to the log file
# RETURN       : SUCCESS/FAIL
###################################################################

def privExecModeWr(logs,session_list):
        buffertrack = ""
        cmd_to_exec = ""
        list_show = []

	# show ineterface command called for a session_id
        if shwc.showIpIntConfigs(logs,session_list[1]) is FAIL:  
                return FAIL

        if shwc.showIpIntConfigs(logs,session_list[2]) is FAIL:
                return FAIL

        if shwc.showIpIntConfigs(logs,session_list[3]) is FAIL: 
                return FAIL

	# interface configuration (telnet_sesion_id, slot, port, ip_address, subnet_mask
        intconf.intfConfigs(logs,session_list[1],1,0,"20.0.0.1","255.255.255.0")   
        intconf.intfConfigs(logs,session_list[1],2,0,"40.0.0.1","255.255.255.0")
        intconf.intfConfigs(logs,session_list[2],1,0,"20.0.0.2","255.255.255.0")
        intconf.intfConfigs(logs,session_list[2],2,0,"30.0.0.1","255.255.255.0")
        intconf.intfConfigs(logs,session_list[3],2,0,"30.0.0.2","255.255.255.0")
	intconf.intfConfigs(logs,session_list[3],3,0,"60.0.0.1","255.255.255.0")
	intconf.intfConfigs(logs,session_list[4],1,0,"40.0.0.2","255.255.255.0")
	intconf.intfConfigs(logs,session_list[4],2,0,"50.0.0.1","255.255.255.0")
	intconf.intfConfigs(logs,session_list[5],2,0,"50.0.0.2","255.255.255.0")
	intconf.intfConfigs(logs,session_list[5],1,0,"60.0.0.2","255.255.255.0")

        if shwc.showIpIntConfigs(logs,session_list[1]) is FAIL:
                return FAIL

        if shwc.showIpIntConfigs(logs,session_list[2]) is FAIL:
                return FAIL

        if shwc.showIpIntConfigs(logs,session_list[3]) is FAIL:
                return FAIL
       
	if shwc.showIpIntConfigs(logs,session_list[4]) is FAIL:
                return FAIL
	
	if shwc.showIpIntConfigs(logs,session_list[5]) is FAIL:
                return FAIL
 
	# check ping to an IP_ADDRESS on a telnet session 
	if png.chkPing(logs,session_list[1],"20.0.0.2") is FAIL:
		print "\nERROR : PING RETURNED FAILURE"
	
	if png.chkPing(logs,session_list[1],"40.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"
	
	if png.chkPing(logs,session_list[2],"30.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"
	
	if png.chkPing(logs,session_list[3],"60.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"
		
	if png.chkPing(logs,session_list[4],"50.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        return SUCCESS


