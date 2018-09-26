SUCCESS = 1
FAIL = 0

global PING_STAT
global PRIV_EXECM
global GLOBAL_EXECM
global INTF_CONFM
global ROUTER_CONFM

def initPingStat():
	global PING_STAT
	PING_STAT = 0

def initPrivExec():
	global PRIV_EXECM
	PRIV_EXECM = 0

def initGlbExec():
	global GLOBAL_EXECM
	GLOBAL_EXECM = 0

def initInfConf():
	global INTF_CONFM
	INTF_CONFM = 0

def initRouterConf():
	global ROUTER_CONFM
	ROUTER_CONFM = 0

def valGlbExec():
	global GLOBAL_EXECM
	if GLOBAL_EXECM == 1:
		return SUCCESS
	else:
		return FAIL

def valInfConf():
	global INTF_CONFM
	if INTF_CONFM == 1:
		return SUCCESS
	else:
		return FAIL

def valRouterConf():
	global ROUTER_CONFM
	if ROUTER_CONFM == 1:
		return SUCCESS
	else:
		return FAIL

def valPrivExec():
	global PRIV_EXECM
	if PRIV_EXECM == 1:
		return SUCCESS
	else:
		return FAIL
