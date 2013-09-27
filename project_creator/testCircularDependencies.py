#!/usr/bin/python3
import utils
import sys
#Test for utils.readCircularDependenciesFromTattletale
#sys.argv[1]: file name
if __name__ == '__main__':
	print(utils.readCircularDependenciesFromTattletale(sys.argv[1]))
