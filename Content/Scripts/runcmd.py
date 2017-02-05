#ue.exec('pip2.py')

import subprocess
import sys
import unreal_engine as ue
import _thread as thread

ue.log(sys.path)

def FolderCommand(folder):
	#replace backslashes
	folder = folder.replace('/','\\')

	changefolder = "cd /d \"" + folder + "\" & "
	return changefolder

def run(process, folder=sys.path[1]):
	#todo: change folder
	fullcommand = FolderCommand(folder) + process
	ue.log("Command <" + fullcommand + ">")
	stdoutdata = subprocess.getstatusoutput(fullcommand)
	ue.log("Command Result: ")
	ue.log(stdoutdata[1])


def Test():
	#debug test - 
	run('dir')	