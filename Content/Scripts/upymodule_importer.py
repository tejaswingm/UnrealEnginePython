#Imports upymodule.json modules and resolves dependencies

#example test
#import upymodule_importer as upym
#upym.parseJson("D:/Users/Admin/Documents/GitHub/tensorflow-ue4-mnist-example/Plugins/tensorflow-ue4/Content/Scripts/upymodule.json")

import upypip as pip
import unreal_engine as ue
import json

import upypip
pip = upypip.pip

def parseJson(packagePath):
	with open(packagePath) as data_file:
		#TODO: catch file not found error    
		package = json.load(data_file)
		ue.log('resolving upymodule dependencies ' + package['name'])
		pythonModules = package['pythonModules']

		#loop over all the modules, check if we have them installed
		for module in pythonModules:
			version = pythonModules[module]

			ue.log(module + " " + version + " installed? " + str(pip.isInstalled(module)))
			if not pip.isInstalled(module):
				ue.log('Dependency not installed, fetching via pip...')
				pip.install(module + '==' + version)
			else:
				ue.log('Already Installed, skipping.')
