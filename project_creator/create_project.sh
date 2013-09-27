#!/bin/bash
#Parameters:
#$1: project path - USE ABSOLUTE PATHS
#$2: ear name, es: nome.ear
#$3: ear location path, es: /path/to

if [ $# -ne 3 ]
then
  echo "Usage: `basename $0` {project_path} {ear_name} {ear_location_path}"
  exit $E_BADARGS
fi

mkdir $1
EAR_LOCATION=$3/$2
# create tattletale report
java -Xmx512m -jar /home/tito/programs/tattletale-1.2.0.Beta2/tattletale.jar $EAR_LOCATION $1/tattlereport
# create cake report
java -jar /home/tito/programs/jboss-cake/jboss-cake.jar -javaPkgs it:org -input $EAR_LOCATION -output $1/cakereport
#Unzip EAR
DEST_DIR=$1/$2
TEMP_DIR=$1/temp
mkdir $DEST_DIR
unzip $EAR_LOCATION -d $DEST_DIR
mkdir $1/temp
#Uncompress WARs and JARs in temp dir
for i in $( ls $DEST_DIR ); do
	if [[ "$i" == *.war ]]
	then
		mkdir $TEMP_DIR/$i
  		unzip $DEST_DIR/$i -d $TEMP_DIR/$i
	elif [[ "$i" == *.jar ]]
	then
		mkdir $TEMP_DIR/$i
  		unzip $DEST_DIR/$i -d $TEMP_DIR/$i
	fi
done
#remove WARs and JARs from dest_dir
rm $DEST_DIR/*.war 
rm $DEST_DIR/*.jar
#copy unzipped dirs in DEST_DIR 
cp -R $TEMP_DIR/* $DEST_DIR
#remove temporary files
rm -rf $TEMP_DIR
# invoke the creation of analysis file
./createAnalysisFile.py $1 $2

