import runcmd as cmd
import sys
from threading import Thread

#blocking actions, should be run on off-thread
def pipModuleAction(command, args):
	return cmd.run('pip ' + command + ' ' + args, cmd.PythonHomeScriptsPath())

#use this if you need to work on the resulting list to query current dependencies
def listDict():
	#get the list of all the modules from pip
	resultString = pipModuleAction('list','--format=columns')

	#convert to lines for parsing
	lines = resultString.split("\n")
	resultDict = {}

	#exclude first two lines, then pair up the results
	for i in range(2,len(lines)):
		splitEntry = lines[i].split() #split and ignore all whitespace
		resultDict[splitEntry[0]] = splitEntry[1]

	return resultDict


#Threaded actions
def install(module):
	t = Thread(target=pipModuleAction, args=('install',module,))
	t.start()

def uninstall(module):
	t = Thread(target=pipModuleAction, args=('uninstall -y',module,))
	t.start()

def list():
	t = Thread(target=listDict)
	t.start()