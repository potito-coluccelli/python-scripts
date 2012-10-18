#!/usr/bin/python3
import string
import sys
import re

#restituisce un array con artifact e relative versioni
def getArrayLibsVers(filename):
    libsRegExp = re.compile('<artifactId>.*?</artifactId>', re.M)
    versRegExp = re.compile('<version>.*?</version>', re.M)
    with open(filename,'r') as f:
    	content=f.read()
    	return createDict(re.findall(libsRegExp, content),re.findall(versRegExp, content))


#Elimina i duplicati
def createDict(arrayLibs,arrayVers):
	print("arrayLibs",arrayLibs)
	print("arrayVers",arrayVers)
	dictionary={}
	for i in range(len(arrayLibs)):
		print(i)
		dictionary[arrayLibs[i]]=arrayVers[i]
	return dictionary


if __name__ == '__main__':
	dictionary=getArrayLibsVers(sys.argv[1])
	
	print(dictionary)