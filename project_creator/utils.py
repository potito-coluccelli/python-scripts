import re
import glob

def stringify(listOfStrings,cut):
	ret=''
	for strin in listOfStrings:
		if cut:
			splittedPath = re.split('/',strin)
			strin = splittedPath[len(splittedPath)-1]
		ret+=strin+'\n'
	return ret
def stringifyDict(dictz):
	ret = ''
	for key in dictz.keys():
		ret+=key+': '
		for lib in dictz[key]:
			ret+=lib+', '
		ret+='\n'
	return ret


def readUsedComponentFromTattletale(tattletaleFile):
	modsRegExp = re.compile('<module name="(.*?)"/>', re.M)
	with open(tattletaleFile,'r') as f:
		content=f.read()
		#print(content)
		return stringify(re.findall(modsRegExp, content),False)
		
def getFilesWithFilter(path,earInternalPath,filterString,extension):
	exp = path+earInternalPath+filterString+'*.'+extension
	print('DEBUG: getJarsWithFilter - exp: '+exp)
	return stringify(glob.glob(exp),True)

def getJarsWithFilter(path,filterString):
	ret = getFilesWithFilter(path,'/*war/WEB-INF/lib/*',filterString,'jar')
	if len(ret)!=0:
		return ret
	else:
		return 'NON PRESENTE'

def arrayBasedSearch(searchPath, arrayToSearch,earInternalPath,fileExtension):
	ret = ''
	for lib in arrayToSearch:
		print('DEBUG: examining lib: ',lib)
		ret += getFilesWithFilter(searchPath,earInternalPath,lib,fileExtension)
	return ret

def multiplePathSearch(searchPath,arrayToSearch,arrayOfPaths,fileExtension):
	ret = ''
	for xmlPath in arrayOfPaths:
		ret += arrayBasedSearch(searchPath,arrayToSearch,xmlPath,fileExtension)
	return ret

def verifyStringFromCakeReport(file,stringToVerify):
	with open(file) as f:
		html=f.read()
	result = re.search(stringToVerify,html)
	print('DEBUG: result: ')
	print(result)
	if (result != None):
		return 'VERIFICARE'
	return 'NON PREVISTO'

def extractValueaFromLink(arrayLinks):
	#extract valuea from links in array <a href="">VALUE</a>
	linksRe = re.compile('<a href=".*?">(.*?)</a>', re.M)
	stringLinks=stringify(arrayLinks,False)
	return re.findall(linksRe,stringLinks)

def readCircularDependenciesFromTattletale(file):
	with open(file) as f:
		html=f.read()
	#modsRegExp = re.compile('<tr.*?>.*?<td><a href=".*?">(.*?)</a></td>.*?<td>(.*?<a href.*?</a>)*</td>.*?</tr>', re.S)
	#Find all libraries key of the circular dependence
	keyLibsRegExp = re.compile('<tr.*?>.*?<td><a href=".*?">(.*?)</a></td>', re.S)
	keyLibs = re.findall(keyLibsRegExp, html)
	libsDict = dict()
	for key in keyLibs:
		#find lbraries that depends from the key
		regexpStr='<tr.*?>.*?<td><a href=".*?">'+key+'</a></td>.*?<td>(.*?<a href.*?</a>.*?)</td>.*?</tr>'
		#regexpStr='<tr.*?>.*?<td><a href=".*?">'+key+'</a></td>.*?<td>.*?<a href.*?>(.*?)</a>.*?</td>.*?</tr>'
		valueLibsRE = re.compile(regexpStr, re.S)
		valueLibs = re.findall(valueLibsRE, html)
		#print('DEBUG: ',regexpStr)
		libsDict[key]=extractValueaFromLink(valueLibs)
	return stringifyDict(libsDict)