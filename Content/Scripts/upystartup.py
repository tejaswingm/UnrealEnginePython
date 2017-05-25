import sys
import unreal_engine as ue
import json
import upycmd as cmd
from os import listdir

from upypip import pip

def checkPipDirectory():
	#get our python scripts path
	configPath = cmd.PythonPluginScriptPath() + '/upyconfig.json'
	correctPipPath = cmd.PythonHomeScriptsPath()

	#let's test our pip directory path
	try:
		with open(configPath) as data_file:
			configs = json.load(data_file)

			#grab currently stored path
			storedPipPath = configs['pipDirectoryPath']

			print(storedPipPath)
			print(tempPath)

			#compare paths
			if (storedPipPath != correctPipPath):
				#if they don't match, remove the pip module and reinstall pip for this module
				
				libPath = cmd.PythonHomePath() + '/Lib/site-packages'
				dirs = listdir(libPath)
				print(libPath)
				print(dirs)

				tempPath = None
				for directory in dirs:
					if ('pip' in directory and
						directory.endswith('.dist-info')):
						tempPath = libPath + directory

				print(tempPath)
				#rmdir Li
	except:
		e = sys.exc_info()[0]
		ue.log('upyconfig.json error: ' + str(e))

#add any startup action you wish to perform in python
def startup():
	#check that our pip directory matches for pip.exe commands
	checkPipDirectory()
