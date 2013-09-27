#!/usr/bin/python3
import re
import sys

def findFileName(filenameWithExt):
	#input for regexp is like: filename.ext, we need to find: filename
	regecp=re.compile('(.*?)\.([^\.]{3})')
	obj = re.search(regecp,filenameWithExt)
	return obj.group(1)


if __name__ == '__main__':
	# *****************     H O W T O   *********************************
	#generate a script for the project creator, example of use (USE ABSOLUTE PATHS!!!!):
	#find /path/to/searchEars -name "*.ear" | ./script_generator.py create_project.sh /path/to/projectdir
	#sys.argv[1]: script sh to invoke
	#sys.argv[2]: project dir path
	print('DEBUG: started script')
	#Input for regex is like: /path/to/app.ext, we want to split the path in: /path/to and app.ext
	regexp=re.compile('([^/]*$)\n')
	packs = []
	#Read packages and prepare output
	for path in sys.stdin.readlines():
		arr = re.split(regexp,path)
		packs.append([arr[1],arr[0]]) #so that packs[0]=earName nad packs[1]=path
	sys.stdout.write('DEBUG: packs = ')
	print(packs)
	outputFile = sys.argv[2]+'/report_script.sh'
	print('Writing file '+outputFile)
	#Pay attention to duplicates in the output file!!!
	with open(outputFile,'wt') as f:
		f.write('#!/bin/bash\n')
		f.write('cd '+sys.path[0]+'\n')
		for pack in packs:
			f.write('./'+sys.argv[1]+' '+sys.argv[2]+'/'+findFileName(pack[0])+
				' '+pack[0]+' '+pack[1]+'\n')
