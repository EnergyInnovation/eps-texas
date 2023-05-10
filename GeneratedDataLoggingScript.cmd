SPECIAL>LOADMODEL|"EPS.mdl"

SIMULATE>SAVELIST|OutputVarsToExport.lst
SIMULATE>RUNNAME|NoSettings
SIMULATE>READCIN|
MENU>RUN|O
MENU>VDF2TAB|NoSettings.vdfx|NoSettings.tsv|OutputVarsToExport.lst|+!||2020|2050|:NoSettings
FILE>DELETE|NoSettings.vdfx

SIMULATE>RUNNAME|IRA_Moderate_Incentives
SIMULATE>READCIN|IRA_Moderate_Incentives.cin
MENU>RUN|O
MENU>VDF2TAB|IRA_Moderate_Incentives.vdfx|IRA_Moderate_Incentives.tsv|OutputVarsToExport.lst|+!||2020|2050|:IRA_Moderate_Incentives
FILE>DELETE|IRA_Moderate_Incentives.vdfx

SIMULATE>SAVELIST|
