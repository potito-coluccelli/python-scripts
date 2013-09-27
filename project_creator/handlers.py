import utils
import sys

path = '.'
earName = ''
#Modify these to add new files to search
libToRemove = ['wsdl4j','saaj','saaj-impl','jaxrpc','log4j','activation','asm','mail','slf4j','jax-qname',
				'jta','ejb3-persistence','axis-saaj','xalan','ejb','commons-logging','jboss-logging','jboss-common']
libClassloadingProblem = ['concurrent','resolver','servlet','jaxws','stax','xercesImpl','xercesSamples','serializer','xml-apis',
							'jsr181','jaxb-xjc','jaxb-impl','jaxb-api','jaxb1-impl']
xmlFiles = ['application','jboss-app','jboss-web']

#Path where files are searched
libPaths = ['/*war/WEB-INF/lib/*','/*','/lib/*']
xmlPaths = ['/*war/WEB-INF/*','/META-INF/*','/*jar/META-INF/*','/*','/*war/WEB-INF/classes/*']

def getSearchPath():
	return path+'/'+earName

def classloadingIsolationHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),['jboss-classloading'],xmlPaths,'xml')

def componentsHandler(obj):
	#TODO: Per ora ci riferiamo a sys.argv, trovare un modo per gestire questo dal main (v. variables scope o oggetti)
	return utils.readUsedComponentFromTattletale(path+'/tattlereport/jboss-as7/'+earName+'/jboss-deployment-structure.xml')

def springHandler(obj):
	#return utils.getJarsWithFilter(getSearchPath(),'spring')
	return utils.multiplePathSearch(getSearchPath(),['spring'],libPaths,'jar')
	
def hibernateHandler(obj):
	#return utils.getJarsWithFilter(getSearchPath(),'hibernate')
	return utils.multiplePathSearch(getSearchPath(),['hibernate'],libPaths,'jar')

def apacheCxfHandler(obj):
	#return utils.getJarsWithFilter(getSearchPath(),'cxf')
	return utils.multiplePathSearch(getSearchPath(),['cxf'],libPaths,'jar')
	
def libToRemoveHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),libToRemove,libPaths,'jar')

def libClassloadingProblemHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),libClassloadingProblem,libPaths,'jar')

def xmlFilesHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),xmlFiles,xmlPaths,'xml')

def log4jXmlHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),['log4j'],xmlPaths,'xml')

def jdbcDriversHandler(obj):
	return 'NIY: jdbcDriversHandler: '+obj.group(0)

def hibernateSessionHandler(obj):
	return utils.verifyStringFromCakeReport(path+'/cakereport/index.html','org.hibernate.classic.Session')

def circularDependenciesHandler(obj):
	return utils.readCircularDependenciesFromTattletale(path+'/tattlereport/circulardependency/index.html')

def jsfHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),['jsf'],xmlPaths,'jar')

def seamHandler(obj):
	return utils.multiplePathSearch(getSearchPath(),['seam'],libPaths,'jar')