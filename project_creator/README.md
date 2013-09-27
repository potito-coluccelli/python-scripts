Generate a report file (analysis.txt) containing advices to migrate applications to jboss.
Script is unstable, needs bug fixes, better management of command params, and other handlers to manage application issues with classloading.
Needs python3, cake and tattletale to work.
To generate the report, look at create_project.sh and create_project_war.sh scripts. The former is for ear packages while the latter for war packages.
Another useful script is script_generator.py, to use in pipe with other commands to generate a script for the generation of reports of more than one package. Look at the example reported into the script for additional informations.

