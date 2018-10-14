import time 

import showConfigs as shwc
import interface_config as intconf
import connectivity as png
import ripconfig as rip
import ospfconfig as ospf
import eigrpconf as eigrp

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

	intconf.valIntStatus(logs,session_list[1],1,0)
	intconf.valIntStatus(logs,session_list[1],2,0)
	intconf.valIntStatus(logs,session_list[2],1,0)
	intconf.valIntStatus(logs,session_list[2],2,0)
	intconf.valIntStatus(logs,session_list[3],2,0)
	intconf.valIntStatus(logs,session_list[3],3,0)
	intconf.valIntStatus(logs,session_list[4],1,0)
	intconf.valIntStatus(logs,session_list[4],2,0)
	intconf.valIntStatus(logs,session_list[5],2,0)
	intconf.valIntStatus(logs,session_list[5],3,0)

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

	#_____RIP CONFIGUATION_________
	# enable RIPv2 on ROUTER with its sessio id"
	#rip.enableRIP(logs,session_list[1],"20.0.0.0")
	#rip.enableRIP(logs,session_list[1],"40.0.0.0")
	#rip.enableRIP(logs,session_list[2],"20.0.0.0")
	#rip.enableRIP(logs,session_list[2],"30.0.0.0")
	#rip.enableRIP(logs,session_list[3],"30.0.0.0")
	#rip.enableRIP(logs,session_list[3],"60.0.0.0")
	#rip.enableRIP(logs,session_list[4],"40.0.0.0")
	#rip.enableRIP(logs,session_list[4],"50.0.0.0")
	#rip.enableRIP(logs,session_list[5],"50.0.0.0")
	#rip.enableRIP(logs,session_list[5],"60.0.0.0")
	
	#for itr in range(1,len(session_list)):
	#	rip.validateRIP(logs,session_list[itr])

	#_____OSPF CONFIGURATION_______
	#ospf.enableOSPF(logs,session_list[1],"20.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[1],"40.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[2],"20.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[2],"30.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[3],"30.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[3],"60.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[4],"40.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[4],"50.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[5],"50.0.0.0","0.0.0.255")
	#ospf.enableOSPF(logs,session_list[5],"60.0.0.0","0.0.0.255")

	#_____EIGRP CONFIGURATION_______
	eigrp.enableEIGRP(logs,session_list[1],100,"20.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[1],100,"40.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[2],100,"20.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[2],100,"30.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[3],100,"30.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[3],100,"60.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[4],100,"40.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[4],100,"50.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[5],100,"50.0.0.0","0.0.0.255")
	eigrp.enableEIGRP(logs,session_list[5],100,"60.0.0.0","0.0.0.255")

	print "SLEEPING FOR 10secs FOR ROUTES TO CONVERGE"
	time.sleep(60)		


        if png.chkPing(logs,session_list[1],"60.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        if png.chkPing(logs,session_list[2],"50.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        if png.chkPing(logs,session_list[3],"20.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        if png.chkPing(logs,session_list[4],"30.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        if png.chkPing(logs,session_list[5],"40.0.0.2") is FAIL:
                print "\nERROR : PING RETURNED FAILURE"

        return SUCCESS



