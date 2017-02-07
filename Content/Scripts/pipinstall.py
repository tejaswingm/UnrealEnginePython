import runcmd as cmd
import sys
from threading import Thread

def pipModuleAction(command, args):
	return cmd.run('pip ' + command + ' ' + args, cmd.PythonHomeScriptsPath())

def install(module):
	t = Thread(target=pipModuleAction, args=('install',module,))
	t.start()

def uninstall(module):
	t = Thread(target=pipModuleAction, args=('uninstall -y',module,))
	t.start()

def listAction():
	pipModuleAction('list','--format=columns')

def list():
	t = Thread(target=listAction)
	t.start()