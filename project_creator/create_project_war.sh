#!/bin/bash
#Parameters:
#$1: project path - USE ABSOLUTE PATHS
#$2: war name, es: nome.war
#$3: war location path, es: /path/to

if [ $# -ne 3 ]
then
  echo "Usage: `basename $0` {project_path} {war_name} {war_location_path}"
  exit $E_BADARGS
fi

mkdir $1
EAR_LOCATION=$3/$2
# create tattletale report
java -Xmx512m -jar /home/tito/programs/tattletale-1.2.0.Beta2/tattletale.jar $EAR_LOCATION $1/tattlereport
# create cake report
java -jar /home/tito/programs/jboss-cake/jboss-cake.jar -javaPkgs it:org -input $EAR_LOCATION -output $1/cakereport
#Unzip EAR
DEST_DIR=$1/$2/$2

mkdir $1/$2
mkdir $DEST_DIR

TEMP_DIR=$1/temp

unzip $EAR_LOCATION -d $DEST_DIR

# invoke the creation of analysis file
./createAnalysisFile.py $1 $2