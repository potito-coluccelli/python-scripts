#!/usr/bin/python3
import string
import sys
import re
import os
#see handlers.py
import handlers

handlers.path = sys.argv[1]
handlers.earName = sys.argv[2]

def readFileTemplate(templatePath):
	with open(templatePath,'r') as f:
		return f.read()


def createOutputString(templateContent):
	tagsAndHandlers = [('<classloading_isolation>',handlers.classloadingIsolationHandler),
						('<components>',handlers.componentsHandler),
						('<spring>',handlers.springHandler),
						('<jsf>',handlers.jsfHandler),
						('<hibernate>',handlers.hibernateHandler),
						('<apache_cxf>',handlers.apacheCxfHandler),
						('<lib_to_remove>',handlers.libToRemoveHandler),
						('<lib_classloading_problem>',handlers.libClassloadingProblemHandler),
						('<jboss-seam>',handlers.seamHandler),
						('<xml_files>',handlers.xmlFilesHandler),
						('<log4j_xml>',handlers.log4jXmlHandler),
						('<jdbc_drivers>',handlers.jdbcDriversHandler),
						('<hibernate_session>',handlers.hibernateSessionHandler),
						('<circular_dependencies>',handlers.circularDependenciesHandler)]
	ret = templateContent
	for tagz,handler in tagsAndHandlers:
		ret=re.sub(tagz,handler,ret)
	return ret

# ------------------- M A I N ---------------------------
if __name__ == '__main__':
	#sys.argv[1]: project path
	#sys.argv[2]: ear name
	#sys.argv[3]: params
	#Example:
	#./createAnalysisFile.py /home/tito/projects/inail/8280ServiziBE_15/apps/AnagraficaSedeInailAsl  AnagraficaSedeInailAsl-ear.ear
	#Definitions
	

 	#Verify classloading isolation
	#TODO

	##TODO: Read path of base_template.txt from system var CREATE_PROJECT_PATH
	templateContent = readFileTemplate('base_template.txt')
	outputString = createOutputString(templateContent)
	with open(sys.argv[1]+'/analysis.txt','wt') as f:
		f.write(outputString)
	if len(sys.argv)==4 and '-v' in sys.argv[3]:
		print(outputString) 
