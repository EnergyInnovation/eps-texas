SPECIAL>LOADMODEL|"EPS.mdl"

SIMULATE>SAVELIST|OutputVarsToExport-Load.lst
SIMULATE>RUNNAME|NoSettings
SIMULATE>READCIN|
MENU>RUN|O
MENU>VDF2TAB|NoSettings.vdfx|NoSettings.tsv|OutputVarsToExport-Load.lst|+!||2019|2050|:NoSettings
FILE>DELETE|NoSettings.vdfx

SIMULATE>RUNNAME|ElectrifyEverything
SIMULATE>READCIN|ElectrifyEverything.cin
MENU>RUN|O
MENU>VDF2TAB|ElectrifyEverything.vdfx|ElectrifyEverything.tsv|OutputVarsToExport-Load.lst|+!||2019|2050|:ElectrifyEverything
FILE>DELETE|ElectrifyEverything.vdfx

SIMULATE>SAVELIST|
