import upycmd as cmd
import sys
from threading import Thread


class PipInstall:
	#global modules class static variable
	modules = None

	def __init__(self):
		return None

	#blocking actions, should be run on off-thread
	def pipModuleAction(self, command, args):
		return cmd.run('pip ' + command + ' ' + args, cmd.PythonHomeScriptsPath())

	#use this if you need to work on the resulting list to query current dependencies
	def listDict(self):
		#get the list of all the modules from pip
		resultString = self.pipModuleAction('list','--format=columns')

		#convert to lines for parsing
		lines = resultString.split("\n")
		resultDict = {}

		#exclude first two lines, then pair up the results
		for i in range(2,len(lines)):
			splitEntry = lines[i].split() #split and ignore all whitespace
			resultDict[splitEntry[0]] = splitEntry[1]

		#save list to cache
		PipInstall.modules = resultDict
		return resultDict

	def isInstalled(self, module):
		if PipInstall.modules == None:
			PipInstall.modules = self.listDict()
		if module in PipInstall.modules:
			return True
		else:
			return False

	#Threaded actions
	def install(self, module):
		PipInstall.modules = None #our cache is no longer valid
		action = self.pipModuleAction
		t = Thread(target=action, args=('install',module,))
		t.start()

	def uninstall(self, module):
		PipInstall.modules = None #our cache is no longer valid
		action = self.pipModuleAction
		t = Thread(target=action, args=('uninstall -y',module,))
		t.start()

	def list(self):
		action = self.listDict
		t = Thread(target=action)
		t.start()

pip = PipInstall()