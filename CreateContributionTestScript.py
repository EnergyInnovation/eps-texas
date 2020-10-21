# CreateContributionTestScript.py
#
# Developed by Jeffrey Rissman
#
# This is a Python script that is used to generate a Vensim command script.
# The Vensim command script will perform one run with all selected policies
# enabled, one run with all policies disabled (a BAU run),
# and one run with each defined subset (or "group") within the set of selected
# policies turned off or turned on (depending on a user setting in this script).


# File Names
# ----------
# Rather than including input and output file names in the code below, we assign all the file
# names to variables in this section.  This allows the names to be easily changed if desired.
ModelFile = "EPS.mdl" # The name of the Vensim model file (typically with .mdl or .vpm extension)
OutputScript = "GeneratedContributionTestScript.cmd" # The desired filename of the Vensim command script to be generated
RunResultsFile = "ContributionTestResults.tsv" # The desired filename for TSV file containing model run results
OutputVarsFile = "OutputVarsToExport.lst" # The name of the file containing a list of variables to be included in the RunResultsFile
                                          # May optionally also be used as a SAVELIST for Vensim (see below)

# Other Settings
# --------------
RunName = "MostRecentRun" # The desired name for all runs performed.  Used as the filename for the VDF files that Vensim creates
EnableOrDisableGroups = "Enable" # Should each group be enabled or disabled in turn?
								 # Essentially, this is testing either the contribution of a group in the proximity of the
								 # BAU case ("Enable") or in the proximity of a scenario defined in the non-zero values of
								 # the policies listed below ("Disable").
PolicySchedule = 1 # The number of the policy implementation schedule file to be used (in InputData/plcy-schd/FoPITY)


# Index definitions
# -----------------
# Each policy is a Python list.  The numbers below are a key to the meaning of the four entries
# that compose each policy, so we can refer to them by meaningful names in the code.
# Note that the fourth entry in each policy, Settings, is itself a list that contains various
# setting values.  Do not change any names or numbers in this section.
Enabled = 0
LongName = 1
ShortName = 2
Settings = 3
Group = 4


# Policy Options
# --------------
# This section specifies which policies should be included in the Vensim command script
# (called here "enabled" policies) and what setting values for those policies should
# be included.  Unless you are using "Enable" Groups mode, all non-repeating
# combinations of the settings for enabled policies will
# be included in the Vensim command script, so do not enable too many policies at once, or
# Vensim will be unable to complete the necessary runs in a reasonable amount of time.
# Each policy is on a single line:
  # You may change the first entry of each policy to "True" to enable the policy or "False" to disable it.
  # The second and third entries are the long and short name of the policy, used internally by this script.  Do not change these names.
  # The fourth entry in each policy is a list of setting values enclosed with square brackets.
    # You may change these values, add more values (separated by commas), and delete values.
    # Any enabled policy must have a minimum of one setting value.  A policy that is disabled
    # and a policy with a setting of zero produce identical results.
  # The fifth entry in each policy is its group name.  By default, each policy is in its own group (and its subscripts share that group).
    # Change the group names so multiple policies share a name (like "financial policies") to cause them to be enabled or disabled together.

PotentialPolicies = (

	# Transportation Sector Policies
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,VOC]","Conventional Pollutant Standards - LDVs VOCs",[0,1],"Conventional Pollutant Standards - LDVs VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,CO]","Conventional Pollutant Standards - LDVs CO",[0,1],"Conventional Pollutant Standards - LDVs CO"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,NOx]","Conventional Pollutant Standards - LDVs NOx",[0,1],"Conventional Pollutant Standards - LDVs NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,PM10]","Conventional Pollutant Standards - LDVs PM10",[0,1],"Conventional Pollutant Standards - LDVs PM10"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,PM25]","Conventional Pollutant Standards - LDVs PM2.5",[0,1],"Conventional Pollutant Standards - LDVs PM2.5"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,SOx]","Conventional Pollutant Standards - LDVs SOx",[0,1],"Conventional Pollutant Standards - LDVs SOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,BC]","Conventional Pollutant Standards - LDVs BC",[0,1],"Conventional Pollutant Standards - LDVs BC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[LDVs,OC]","Conventional Pollutant Standards - LDVs OC",[0,1],"Conventional Pollutant Standards - LDVs OC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,VOC]","Conventional Pollutant Standards - HDVs VOCs",[0,1],"Conventional Pollutant Standards - HDVs VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,CO]","Conventional Pollutant Standards - HDVs CO",[0,1],"Conventional Pollutant Standards - HDVs CO"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,NOx]","Conventional Pollutant Standards - HDVs NOx",[0,1],"Conventional Pollutant Standards - HDVs NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,PM10]","Conventional Pollutant Standards - HDVs PM10",[0,1],"Conventional Pollutant Standards - HDVs PM10"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,PM25]","Conventional Pollutant Standards - HDVs PM2.5",[0,1],"Conventional Pollutant Standards - HDVs PM2.5"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,SOx]","Conventional Pollutant Standards - HDVs SOx",[0,1],"Conventional Pollutant Standards - HDVs SOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,BC]","Conventional Pollutant Standards - HDVs BC",[0,1],"Conventional Pollutant Standards - HDVs BC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[HDVs,OC]","Conventional Pollutant Standards - HDVs OC",[0,1],"Conventional Pollutant Standards - HDVs OC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[aircraft,VOC]","Conventional Pollutant Standards - aircraft VOCs",[0,1],"Conventional Pollutant Standards - aircraft VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[aircraft,NOx]","Conventional Pollutant Standards - aircraft NOx",[0,1],"Conventional Pollutant Standards - aircraft NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,VOC]","Conventional Pollutant Standards - rail VOCs",[0,1],"Conventional Pollutant Standards - rail VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,CO]","Conventional Pollutant Standards - rail CO",[0,1],"Conventional Pollutant Standards - rail CO"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,NOx]","Conventional Pollutant Standards - rail NOx",[0,1],"Conventional Pollutant Standards - rail NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,PM10]","Conventional Pollutant Standards - rail PM10",[0,1],"Conventional Pollutant Standards - rail PM10"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,PM25]","Conventional Pollutant Standards - rail PM2.5",[0,1],"Conventional Pollutant Standards - rail PM2.5"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,BC]","Conventional Pollutant Standards - rail BC",[0,1],"Conventional Pollutant Standards - rail BC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[rail,OC]","Conventional Pollutant Standards - rail OC",[0,1],"Conventional Pollutant Standards - rail OC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,VOC]","Conventional Pollutant Standards - ships VOCs",[0,1],"Conventional Pollutant Standards - ships VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,CO]","Conventional Pollutant Standards - ships CO",[0,1],"Conventional Pollutant Standards - ships CO"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,NOx]","Conventional Pollutant Standards - ships NOx",[0,1],"Conventional Pollutant Standards - ships NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,PM10]","Conventional Pollutant Standards - ships PM10",[0,1],"Conventional Pollutant Standards - ships PM10"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,PM25]","Conventional Pollutant Standards - ships PM2.5",[0,1],"Conventional Pollutant Standards - ships PM2.5"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,BC]","Conventional Pollutant Standards - ships BC",[0,1],"Conventional Pollutant Standards - ships BC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[ships,OC]","Conventional Pollutant Standards - ships OC",[0,1],"Conventional Pollutant Standards - ships OC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,VOC]","Conventional Pollutant Standards - motorbikes VOCs",[0,1],"Conventional Pollutant Standards - motorbikes VOCs"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,CO]","Conventional Pollutant Standards - motorbikes CO",[0,1],"Conventional Pollutant Standards - motorbikes CO"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,NOx]","Conventional Pollutant Standards - motorbikes NOx",[0,1],"Conventional Pollutant Standards - motorbikes NOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,PM10]","Conventional Pollutant Standards - motorbikes PM10",[0,1],"Conventional Pollutant Standards - motorbikes PM10"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,PM25]","Conventional Pollutant Standards - motorbikes PM2.5",[0,1],"Conventional Pollutant Standards - motorbikes PM2.5"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,SOx]","Conventional Pollutant Standards - motorbikes SOx",[0,1],"Conventional Pollutant Standards - motorbikes SOx"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,BC]","Conventional Pollutant Standards - motorbikes BC",[0,1],"Conventional Pollutant Standards - motorbikes BC"),
	(True,"Percentage Reduction of Separately Regulated Pollutants[motorbikes,OC]","Conventional Pollutant Standards - motorbikes OC",[0,1],"Conventional Pollutant Standards - motorbikes OC"),
	(True,"EV Charger Deployment","Electric Vehicle Charger Deployment",[0,300],"EV Charger Deployment"),
	(True,"Reduce EV Range Anxiety and Charging Time","Electric Vehicle Range n Charging Time",[0,1],"EV Range n Charging Time"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,LDVs]","Electric Vehicle Sales Mandate - Passenger LDVs",[0,1],"Electric Vehicle Sales Mandate - Passenger LDVs"),
	(True,"Additional Minimum Required EV Sales Percentage[freight,LDVs]","Electric Vehicle Sales Mandate - Freight LDVs",[0,1],"Electric Vehicle Sales Mandate - Freight LDVs"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,HDVs]","Electric Vehicle Sales Mandate - Passenger HDVs",[0,1],"Electric Vehicle Sales Mandate - Passenger HDVs"),
	(True,"Additional Minimum Required EV Sales Percentage[freight,HDVs]","Electric Vehicle Sales Mandate - Freight HDVs",[0,1],"Electric Vehicle Sales Mandate - Freight HDVs"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,aircraft]","Electric Vehicle Sales Mandate - Passenger Aircraft",[0,1],"Electric Vehicle Sales Mandate - Passenger Aircraft"),
	(True,"Additional Minimum Required EV Sales Percentage[freight,aircraft]","Electric Vehicle Sales Mandate - Freight Aircraft",[0,1],"Electric Vehicle Sales Mandate - Freight Aircraft"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,rail]","Electric Vehicle Sales Mandate - Passenger Rail",[0,1],"Electric Vehicle Sales Mandate - Passenger Rail"),
	(True,"Additional Minimum Required EV Sales Percentage[freight,rail]","Electric Vehicle Sales Mandate - Freight Rail",[0,1],"Electric Vehicle Sales Mandate - Freight Rail"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,ships]","Electric Vehicle Sales Mandate - Passenger Ships",[0,1],"Electric Vehicle Sales Mandate - Passenger Ships"),
	(True,"Additional Minimum Required EV Sales Percentage[freight,ships]","Electric Vehicle Sales Mandate - Freight Ships",[0,1],"Electric Vehicle Sales Mandate - Freight Ships"),
	(True,"Additional Minimum Required EV Sales Percentage[passenger,motorbikes]","Electric Vehicle Sales Mandate - Passenger Motorbikes",[0,1],"Electric Vehicle Sales Mandate - Passenger Motorbikes"),
	(True,"Additional EV Subsidy Percentage[passenger,LDVs]","Electric Vehicle Subsidy - Passenger LDVs",[0,0.5],"EV Subsidy"),
	(True,"LDVs Feebate Rate","Feebate",[0,1],"Feebate"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,LDVs]","Fuel Economy Standard - Passenger LDVs",[0,1],"Fuel Economy Standard - Passenger LDVs"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,LDVs]","Fuel Economy Standard - Freight LDVs",[0,1],"Fuel Economy Standard - Freight LDVs"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,HDVs]","Fuel Economy Standard - Passenger HDVs",[0,0.66],"Fuel Economy Standard - Passenger HDVs"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,HDVs]","Fuel Economy Standard - Freight HDVs",[0,0.66],"Fuel Economy Standard - Freight HDVs"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,aircraft]","Fuel Economy Standard - Passenger Aircraft",[0,0.54],"Fuel Economy Standard - Passenger Aircraft"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,aircraft]","Fuel Economy Standard - Freight Aircraft",[0,0.54],"Fuel Economy Standard - Freight Aircraft"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,rail]","Fuel Economy Standard - Passenger Rail",[0,0.2],"Fuel Economy Standard - Passenger Rail"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,rail]","Fuel Economy Standard - Freight Rail",[0,0.2],"Fuel Economy Standard - Freight Rail"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,ships]","Fuel Economy Standard - Passenger Ships",[0,0.2],"Fuel Economy Standard - Passenger Ships"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[freight,ships]","Fuel Economy Standard - Freight Ships",[0,0.2],"Fuel Economy Standard - Freight Ships"),
	(True,"Percentage Additional Improvement of Fuel Economy Std[passenger,motorbikes]","Fuel Economy Standard - Passenger Motorbikes",[0,0.74],"Fuel Economy Standard - Passenger Motorbikes"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,LDVs]","Hydrogen Vehicle Sales Mandate - Passenger LDVs",[0,1],"Hydrogen Vehicle Sales Mandate - Passenger LDVs"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,LDVs]","Hydrogen Vehicle Sales Mandate - Freight LDVs",[0,1],"Hydrogen Vehicle Sales Mandate - Freight LDVs"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,HDVs]","Hydrogen Vehicle Sales Mandate - Passenger HDVs",[0,1],"Hydrogen Vehicle Sales Mandate - Passenger HDVs"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,HDVs]","Hydrogen Vehicle Sales Mandate - Freight HDVs",[0,1],"Hydrogen Vehicle Sales Mandate - Freight HDVs"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,aircraft]","Hydrogen Vehicle Sales Mandate - Passenger Aircraft",[0,1],"Hydrogen Vehicle Sales Mandate - Passenger Aircraft"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,aircraft]","Hydrogen Vehicle Sales Mandate - Freight Aircraft",[0,1],"Hydrogen Vehicle Sales Mandate - Freight Aircraft"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,rail]","Hydrogen Vehicle Sales Mandate - Passenger Rail",[0,1],"Hydrogen Vehicle Sales Mandate - Passenger Rail"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,rail]","Hydrogen Vehicle Sales Mandate - Freight Rail",[0,1],"Hydrogen Vehicle Sales Mandate - Freight Rail"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[passenger,ships]","Hydrogen Vehicle Sales Mandate - Passenger Ships",[0,1],"Hydrogen Vehicle Sales Mandate - Passenger Ships"),
	(True,"Minimum Required Hydrogen Vehicle Sales Percentage[freight,ships]","Hydrogen Vehicle Sales Mandate - Freight Ships",[0,1],"Hydrogen Vehicle Sales Mandate - Freight Ships"),
	(True,"Additional LCFS Percentage","Low Carbon Fuel Standard",[0,0.2],"Low Carbon Fuel Standard"),
	(True,"Fraction of TDM Package Implemented[passenger]","Transportation Demand Management - Passengers",[0,1],"Transportation Demand Management - Passengers"),
	(True,"Fraction of TDM Package Implemented[freight]","Transportation Demand Management - Freight",[0,1],"Transportation Demand Management - Freight"),

	# Buildings Sector Policies
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[heating,urban residential]","Building Component Electrification - Urban Residential Heating",[0,1],"Building Component Electrification - Urban Residential Heating"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[appliances,urban residential]","Building Component Electrification - Urban Residential Appliances",[0,1],"Building Component Electrification - Urban Residential Appliances"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[other component,urban residential]","Building Component Electrification - Urban Residential Other Components",[0,1],"Building Component Electrification - Urban Residential Other Components"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[heating,rural residential]","Building Component Electrification - Rural Residential Heating",[0,1],"Building Component Electrification - Rural Residential Heating"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[appliances,rural residential]","Building Component Electrification - Rural Residential Appliances",[0,1],"Building Component Electrification - Rural Residential Appliances"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[other component,rural residential]","Building Component Electrification - Rural Residential Other Components",[0,1],"Building Component Electrification - Rural Residential Other Components"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[heating,commercial]","Building Component Electrification - Commercial Heating",[0,1],"Building Component Electrification - Commercial Heating"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[appliances,commercial]","Building Component Electrification - Commercial Appliances",[0,1],"Building Component Electrification - Commercial Appliances"),
	(True,"Fraction of New Bldg Components Shifted to Other Fuels[other component,commercial]","Building Component Electrification - Commercial Other Components",[0,1],"Building Component Electrification - Commercial Other Components"),
	(True,"Reduction in E Use Allowed by Component Eff Std[heating,urban residential]","Building Energy Efficiency Standards - Urban Residential Heating",[0,0.22],"Building Energy Efficiency Standards - Urban Residential Heating"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,urban residential]","Building Energy Efficiency Standards - Urban Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards - Urban Residential Cooling and Ventilation"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,urban residential]","Building Energy Efficiency Standards - Urban Residential Envelope",[0,0.38],"Building Energy Efficiency Standards - Urban Residential Envelope"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,urban residential]","Building Energy Efficiency Standards - Urban Residential Lighting",[0,0.4],"Building Energy Efficiency Standards - Urban Residential Lighting"),
	(True,"Reduction in E Use Allowed by Component Eff Std[appliances,urban residential]","Building Energy Efficiency Standards - Urban Residential Appliances",[0,0.38],"Building Energy Efficiency Standards - Urban Residential Appliances"),
	(True,"Reduction in E Use Allowed by Component Eff Std[other component,urban residential]","Building Energy Efficiency Standards - Urban Residential Other Components",[0,0.11],"Building Energy Efficiency Standards - Urban Residential Other Components"),
	(True,"Reduction in E Use Allowed by Component Eff Std[heating,rural residential]","Building Energy Efficiency Standards - Rural Residential Heating",[0,0.22],"Building Energy Efficiency Standards - Rural Residential Heating"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,rural residential]","Building Energy Efficiency Standards - Rural Residential Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards - Rural Residential Cooling and Ventilation"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,rural residential]","Building Energy Efficiency Standards - Rural Residential Envelope",[0,0.38],"Building Energy Efficiency Standards - Rural Residential Envelope"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,rural residential]","Building Energy Efficiency Standards - Rural Residential Lighting",[0,0.4],"Building Energy Efficiency Standards - Rural Residential Lighting"),
	(True,"Reduction in E Use Allowed by Component Eff Std[appliances,rural residential]","Building Energy Efficiency Standards - Rural Residential Appliances",[0,0.38],"Building Energy Efficiency Standards - Rural Residential Appliances"),
	(True,"Reduction in E Use Allowed by Component Eff Std[other component,rural residential]","Building Energy Efficiency Standards - Rural Residential Other Components",[0,0.11],"Building Energy Efficiency Standards - Rural Residential Other Components"),
	(True,"Reduction in E Use Allowed by Component Eff Std[heating,commercial]","Building Energy Efficiency Standards - Commercial Heating",[0,0.22],"Building Energy Efficiency Standards - Commercial Heating"),
	(True,"Reduction in E Use Allowed by Component Eff Std[cooling and ventilation,commercial]","Building Energy Efficiency Standards - Commercial Cooling and Ventilation",[0,0.38],"Building Energy Efficiency Standards - Commercial Cooling and Ventilation"),
	(True,"Reduction in E Use Allowed by Component Eff Std[envelope,commercial]","Building Energy Efficiency Standards - Commercial Envelope",[0,0.38],"Building Energy Efficiency Standards - Commercial Envelope"),
	(True,"Reduction in E Use Allowed by Component Eff Std[lighting,commercial]","Building Energy Efficiency Standards - Commercial Lighting",[0,0.4],"Building Energy Efficiency Standards - Commercial Lighting"),
	(True,"Reduction in E Use Allowed by Component Eff Std[appliances,commercial]","Building Energy Efficiency Standards - Commercial Appliances",[0,0.38],"Building Energy Efficiency Standards - Commercial Appliances"),
	(True,"Reduction in E Use Allowed by Component Eff Std[other component,commercial]","Building Energy Efficiency Standards - Commercial Other Components",[0,0.11],"Building Energy Efficiency Standards - Commercial Other Components"),
	(True,"Boolean Improved Contractor Edu and Training","Contractor Training",[0,1],"Contractor Training"),
	(True,"Min Fraction of Total Elec Demand to be Met by Distributed Solar PV","Distributed Solar Carve-Out",[0,0.24],"Distributed Solar Carve-Out"),
	(True,"Perc Subsidy for Distributed Solar PV Capacity","Distributed Solar Subsidy",[0,0.5],"Distributed Solar Subsidy"),
	(True,"Boolean Improved Device Labeling","Improved Labeling",[0,1],"Improved Labeling"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[urban residential]","Retrofit Existing Buildings - Urban Residential",[0,0.5],"Retrofit Existing Buildings - Urban Residential"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[rural residential]","Retrofit Existing Buildings - Rural Residential",[0,0.5],"Retrofit Existing Buildings - Rural Residential"),
	(True,"Share of Preexisting Buildings Subject to Retrofitting[commercial]","Retrofit Existing Buildings - Commercial",[0,0.5],"Retrofit Existing Buildings - Commercial"),
	(True,"Boolean Rebate Program for Efficient Components[heating]","Rebate for Efficient Products - Heating",[0,1],"Rebate for Efficient Products - Heating"),
	(True,"Boolean Rebate Program for Efficient Components[cooling and ventilation]","Rebate for Efficient Products - Cooling and Ventilation",[0,1],"Rebate for Efficient Products - Cooling and Ventilation"),
	(True,"Boolean Rebate Program for Efficient Components[appliances]","Rebate for Efficient Products - Appliances",[0,1],"Rebate for Efficient Products - Appliances"),

	# Electricity Sector Policies
	(True,"Boolean Ban New Power Plants[hard coal es]","Ban New Power Plants - Hard Coal",[0,1],"Ban New Power Plants - Hard Coal"),
	(True,"Boolean Ban New Power Plants[natural gas nonpeaker es]","Ban New Power Plants - Natural Gas Nonpeaker",[0,1],"Ban New Power Plants - Natural Gas Nonpeaker"),
	(True,"Boolean Ban New Power Plants[nuclear es]","Ban New Power Plants - Nuclear",[0,1],"Ban New Power Plants - Nuclear"),
	(True,"Boolean Ban New Power Plants[hydro es]","Ban New Power Plants - Hydro",[0,1],"Ban New Power Plants - Hydro"),
	(True,"Boolean Ban New Power Plants[lignite es]","Ban New Power Plants - Lignite",[0,1],"Ban New Power Plants - Lignite"),
	(True,"Renewable Portfolio Std Percentage","Carbon-free Electricity Standard",[0,1],"Carbon-free Electricity Standard"),
	(True,"Percent Change in Electricity Exports","Change Electricity Exports",[-0.5,1],"Change Electricity Exports"),
	(True,"Percent Change in Electricity Imports[hard coal es]","Change Electricity Imports - Hard Coal",[-0.5,1],"Change Electricity Imports - Hard Coal"),
	(True,"Percent Change in Electricity Imports[natural gas nonpeaker es]","Change Electricity Imports - Natural Gas Nonpeaker",[-0.5,1],"Change Electricity Imports - Natural Gas Nonpeaker"),
	(True,"Percent Change in Electricity Imports[nuclear es]","Change Electricity Imports - Nuclear",[-0.5,1],"Change Electricity Imports - Nuclear"),
	(True,"Percent Change in Electricity Imports[hydro es]","Change Electricity Imports - Hydro",[-0.5,1],"Change Electricity Imports - Hydro"),
	(True,"Percent Change in Electricity Imports[onshore wind es]","Change Electricity Imports - Onshore Wind",[-0.5,1],"Change Electricity Imports - Onshore Wind"),
	(True,"Percent Change in Electricity Imports[solar PV es]","Change Electricity Imports - Solar PV",[-0.5,1],"Change Electricity Imports - Solar PV"),
	(True,"Percent Change in Electricity Imports[biomass es]","Change Electricity Imports - Biomass",[-0.5,1],"Change Electricity Imports - Biomass"),
	(True,"Percent Change in Electricity Imports[petroleum es]","Change Electricity Imports - Petroleum",[-0.5,1],"Change Electricity Imports - Petroleum"),
	(True,"Fraction of Additional Demand Response Potential Achieved","Demand Response",[0,1],"Demand Response"),
	(True,"Annual Additional Capacity Retired due to Early Retirement Policy[hard coal es]","Early Retirement of Power Plants - Hard Coal",[0,10000],"Early Retirement of Power Plants - Hard Coal"),
	(True,"Annual Additional Capacity Retired due to Early Retirement Policy[nuclear es]","Early Retirement of Power Plants - Nuclear",[0,10000],"Early Retirement of Power Plants - Nuclear"),
	(True,"Additional Battery Storage Annual Growth Percentage","Grid-Scale Electricity Storage",[0,0.16],"Grid-Scale Electricity Storage"),
	(True,"Percentage Increase in Transmission Capacity vs BAU","Increase Transmission",[0,1.13],"Increase Transmission"),
	(True,"Percentage Reduction in Plant Downtime[natural gas nonpeaker es,preexisting retiring]","Reduce Plant Downtime - Preexisting Natural Gas Nonpeaker",[0,0.6],"Reduce Plant Downtime - Preexisting Natural Gas Nonpeaker"),
	(True,"Percentage Reduction in Plant Downtime[onshore wind es,newly built]","Reduce Plant Downtime - New Onshore Wind",[0,0.25],"Reduce Plant Downtime - New Onshore Wind"),
	(True,"Percentage Reduction in Plant Downtime[solar PV es,newly built]","Reduce Plant Downtime - New Solar PV",[0,0.3],"Reduce Plant Downtime - New Solar PV"),
	(True,"Percentage Reduction in Plant Downtime[offshore wind es,newly built]","Reduce Plant Downtime - New Offshore Wind",[0,0.25],"Reduce Plant Downtime - New Offshore Wind"),
	(True,"Percent Reduction in Soft Costs of Capacity Construction[onshore wind es]","Reduce Soft Costs - Onshore Wind",[0,0.9],"Reduce Soft Costs - Onshore Wind"),
	(True,"Percent Reduction in Soft Costs of Capacity Construction[solar PV es]","Reduce Soft Costs - Solar PV",[0,0.9],"Reduce Soft Costs - Solar PV"),
	(True,"Percent Reduction in Soft Costs of Capacity Construction[offshore wind es]","Reduce Soft Costs - Offshore Wind",[0,0.9],"Reduce Soft Costs - Offshore Wind"),
	(True,"Percentage TnD Losses Avoided","Reduce Transmission n Distribution Losses",[0,0.4],"Reduce TnD Losses"),
	(True,"Subsidy for Elec Production by Fuel[nuclear es]","Subsidy for Electricity Production - Nuclear",[0,60],"Subsidy for Electricity Production - Nuclear"),
	(True,"Subsidy for Elec Production by Fuel[onshore wind es]","Subsidy for Electricity Production - Onshore Wind",[0,60],"Subsidy for Electricity Production - Onshore Wind"),
	(True,"Subsidy for Elec Production by Fuel[solar PV es]","Subsidy for Electricity Production - Solar PV",[0,60],"Subsidy for Electricity Production - Solar PV"),
	(True,"Subsidy for Elec Production by Fuel[solar thermal es]","Subsidy for Electricity Production - Solar Thermal",[0,60],"Subsidy for Electricity Production - Solar Thermal"),
	(True,"Subsidy for Elec Production by Fuel[biomass es]","Subsidy for Electricity Production - Biomass",[0,60],"Subsidy for Electricity Production - Biomass"),
	(True,"Subsidy for Elec Production by Fuel[offshore wind es]","Subsidy for Electricity Production - Offshore Wind",[0,60],"Subsidy for Electricity Production - Offshore Wind"),

	# Industry Sector Policies
	(True,"Fraction of Cement Measures Achieved","Cement Clinker Substitution",[0,1],"Cement Clinker Substitution"),
	(True,"Fraction of Potential Cogeneration and Waste Heat Recovery Adopted","Cogeneration and Waste Heat Recovery",[0,1],"Cogeneration and Waste Heat Recovery"),
	(True,"Fraction of Energy Savings from Early Facility Retirement Achieved","Early Retirement of Industrial Facilities",[0,1],"Early Retirement of Industrial Facilities"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[cement and other carbonates]","Industry Energy Efficiency Standards - Cement Industry",[0,0.33],"Industry Energy Efficiency Standards - Cement Industry"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[natural gas and petroleum systems]","Industry Energy Efficiency Standards - Natural Gas and Petroleum Industry",[0,0.33],"Industry Energy Efficiency Standards - Natural Gas and Petroleum Industry"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[iron and steel]","Industry Energy Efficiency Standards - Iron and Steel Industry",[0,0.33],"Industry Energy Efficiency Standards - Iron and Steel Industry"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[chemicals]","Industry Energy Efficiency Standards - Chemicals Industry",[0,0.33],"Industry Energy Efficiency Standards - Chemicals Industry"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[coal mining]","Industry Energy Efficiency Standards - Mining Industry",[0,0.33],"Industry Energy Efficiency Standards - Mining Industry"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[waste management]","Industry Energy Efficiency Standards - Water n Waste",[0,0.33],"Industry Energy Efficiency Standards - Water n Waste"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[agriculture]","Industry Energy Efficiency Standards - Agriculture",[0,0.33],"Industry Energy Efficiency Standards - Agriculture"),
	(True,"Percentage Improvement in Eqpt Efficiency Standards above BAU[other industries]","Industry Energy Efficiency Standards - Other Industries",[0,0.33],"Industry Energy Efficiency Standards - Other Industries"),
	(True,"Fraction of Installation and System Integration Issues Remedied","Improved System Design",[0,1],"Improved System Design"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,hard coal if]","Electrification + Hydrogen - Cement Industry Coal Use",[0,1],"Electrification + Hydrogen - Cement Industry Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,natural gas if]","Electrification + Hydrogen - Cement Industry Natural Gas Use",[0,1],"Electrification + Hydrogen - Cement Industry Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,petroleum diesel if]","Electrification + Hydrogen - Cement Industry Petroleum Use",[0,1],"Electrification + Hydrogen - Cement Industry Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,heavy or residual fuel oil if]","Electrification + Hydrogen - Cement Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Cement Industry Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[cement and other carbonates,LPG propane or butane if]","Electrification + Hydrogen - Cement Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen - Cement Industry LPG Propane or Butane Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,hard coal if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Coal Use",[0,1],"Electrification + Hydrogen - Natural Gas and Petroleum Industry Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,natural gas if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Natural Gas Use",[0,1],"Electrification + Hydrogen - Natural Gas and Petroleum Industry Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,biomass if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Biomass Use",[0,1],"Electrification + Hydrogen - Natural Gas and Petroleum Industry Biomass Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,petroleum diesel if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Petroleum Use",[0,1],"Electrification + Hydrogen - Natural Gas and Petroleum Industry Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[natural gas and petroleum systems,crude oil if]","Electrification + Hydrogen - Natural Gas and Petroleum Industry Crude Oil Use",[0,1],"Electrification + Hydrogen - Natural Gas and Petroleum Industry Crude Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,hard coal if]","Electrification + Hydrogen - Iron and Steel Industry Coal Use",[0,1],"Electrification + Hydrogen - Iron and Steel Industry Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,natural gas if]","Electrification + Hydrogen - Iron and Steel Industry Natural Gas Use",[0,1],"Electrification + Hydrogen - Iron and Steel Industry Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,petroleum diesel if]","Electrification + Hydrogen - Iron and Steel Industry Petroleum Use",[0,1],"Electrification + Hydrogen - Iron and Steel Industry Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,heavy or residual fuel oil if]","Electrification + Hydrogen - Iron and Steel Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Iron and Steel Industry Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[iron and steel,LPG propane or butane if]","Electrification + Hydrogen - Iron and Steel Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen - Iron and Steel Industry LPG Propane or Butane Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,hard coal if]","Electrification + Hydrogen - Chemicals Industry Coal Use",[0,1],"Electrification + Hydrogen - Chemicals Industry Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,natural gas if]","Electrification + Hydrogen - Chemicals Industry Natural Gas Use",[0,1],"Electrification + Hydrogen - Chemicals Industry Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,petroleum diesel if]","Electrification + Hydrogen - Chemicals Industry Petroleum Use",[0,1],"Electrification + Hydrogen - Chemicals Industry Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,heavy or residual fuel oil if]","Electrification + Hydrogen - Chemicals Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Chemicals Industry Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[chemicals,LPG propane or butane if]","Electrification + Hydrogen - Chemicals Industry LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen - Chemicals Industry LPG Propane or Butane Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,hard coal if]","Electrification + Hydrogen - Mining Industry Coal Use",[0,1],"Electrification + Hydrogen - Mining Industry Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,natural gas if]","Electrification + Hydrogen - Mining Industry Natural Gas Use",[0,1],"Electrification + Hydrogen - Mining Industry Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,petroleum diesel if]","Electrification + Hydrogen - Mining Industry Petroleum Use",[0,1],"Electrification + Hydrogen - Mining Industry Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[coal mining,heavy or residual fuel oil if]","Electrification + Hydrogen - Mining Industry Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Mining Industry Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,natural gas if]","Electrification + Hydrogen - Agriculture Natural Gas Use",[0,1],"Electrification + Hydrogen - Agriculture Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,petroleum diesel if]","Electrification + Hydrogen - Agriculture Petroleum Use",[0,1],"Electrification + Hydrogen - Agriculture Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,heavy or residual fuel oil if]","Electrification + Hydrogen - Agriculture Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Agriculture Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[agriculture,LPG propane or butane if]","Electrification + Hydrogen - Agriculture LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen - Agriculture LPG Propane or Butane Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,hard coal if]","Electrification + Hydrogen - Other Industries Coal Use",[0,1],"Electrification + Hydrogen - Other Industries Coal Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,natural gas if]","Electrification + Hydrogen - Other Industries Natural Gas Use",[0,1],"Electrification + Hydrogen - Other Industries Natural Gas Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,petroleum diesel if]","Electrification + Hydrogen - Other Industries Petroleum Use",[0,1],"Electrification + Hydrogen - Other Industries Petroleum Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,heavy or residual fuel oil if]","Electrification + Hydrogen - Other Industries Heavy or Residual Fuel Oil Use",[0,1],"Electrification + Hydrogen - Other Industries Heavy or Residual Fuel Oil Use"),
	(True,"Fraction of Industrial Fuel Use Shifted to Other Fuels[other industries,LPG propane or butane if]","Electrification + Hydrogen - Other Industries LPG Propane or Butane Use",[0,1],"Electrification + Hydrogen - Other Industries LPG Propane or Butane Use"),
	(True,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[cement and other carbonates]","Material Efficiency, Longevity, n Re-Use - Cement Industry",[0,1],"Material Efficiency, Longevity, n Re-Use - Cement Industry"),
	(True,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[iron and steel]","Material Efficiency, Longevity, n Re-Use - Iron and Steel Industry",[0,1],"Material Efficiency, Longevity, n Re-Use - Iron and Steel Industry"),
	(True,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[chemicals]","Material Efficiency, Longevity, n Re-Use - Chemicals Industry",[0,1],"Material Efficiency, Longevity, n Re-Use - Chemicals Industry"),
	(True,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[waste management]","Material Efficiency, Longevity, n Re-Use - Water n Waste",[0,1],"Material Efficiency, Longevity, n Re-Use - Water n Waste"),
	(True,"Percent Reduction in Nonenergy Nonagriculture Industry Product Demand[other industries]","Material Efficiency, Longevity, n Re-Use - Other Industries",[0,1],"Material Efficiency, Longevity, n Re-Use - Other Industries"),
	(True,"Fraction of Methane Capture Opportunities Achieved[natural gas and petroleum systems]","Methane Capture - Natural Gas and Petroleum",[0,1],"Methane Capture and Destruction"),
	(True,"Fraction of Methane Capture Opportunities Achieved[coal mining]","Methane Capture - Coal",[0,1],"Methane Capture - Natural Gas and Petroleum"),
	(True,"Fraction of Methane Capture Opportunities Achieved[waste management]","Methane Capture - Waste",[0,1],"Methane Capture - Coal"),
	(True,"Fraction of Methane Destruction Opportunities Achieved[natural gas and petroleum systems","Methane Destruction - Natural Gas and Petroleum",[0,1],"Methane Destruction - Natural Gas and Petroleum"),
	(True,"Fraction of Methane Destruction Opportunities Achieved[coal mining]","Methane Destruction - Coal",[0,1],"Methane Destruction - Coal"),
	(True,"Fraction of Methane Destruction Opportunities Achieved[waste management","Methane Destruction - Waste",[0,1],"Methane Destruction - Waste"),
	(True,"Fraction of F Gas Substitution Achieved","F-gas substitution",[0,1],"F-gas substitution"),
	(True,"Fraction of F Gas Recovery Achieved","F-gas recovery",[0,1],"F-gas recovery"),
	(True,"Fraction of F Gas Destruction Achieved","F-gas destruction",[0,1],"F-gas destruction"),
	(True,"Fraction of F Gas Inspct Maint Retrofit Achieved","F-gas inspct",[0,1],"F-gas inspct"),
	(True,"Percent Reduction in Fossil Fuel Exports[hard coal]","Reduce Fossil Fuel Exports - Hard Coal",[0,1],"Reduce Fossil Fuel Exports - Hard Coal"),
	(True,"Percent Reduction in Fossil Fuel Exports[natural gas]","Reduce Fossil Fuel Exports - Natural Gas",[0,1],"Reduce Fossil Fuel Exports - Natural Gas"),
	(True,"Percent Reduction in Fossil Fuel Exports[petroleum gasoline]","Reduce Fossil Fuel Exports - Petroleum Gasoline",[0,1],"Reduce Fossil Fuel Exports - Petroleum Gasoline"),
	(True,"Percent Reduction in Fossil Fuel Exports[petroleum diesel]","Reduce Fossil Fuel Exports - Petroleum Diesel",[0,1],"Reduce Fossil Fuel Exports - Petroleum Diesel"),
	(True,"Percent Reduction in Fossil Fuel Exports[jet fuel or kerosene]","Reduce Fossil Fuel Exports - Jet Fuel/Kerosene",[0,1],"Reduce Fossil Fuel Exports - Jet Fuel/Kerosene"),
	(True,"Percent Reduction in Fossil Fuel Exports[crude oil]","Reduce Fossil Fuel Exports - Crude Oil",[0,1],"Reduce Fossil Fuel Exports - Crude Oil"),
	(True,"Percent Reduction in Fossil Fuel Exports[heavy or residual fuel oil]","Reduce Fossil Fuel Exports - Heavy/Residual Fuel Oil",[0,1],"Reduce Fossil Fuel Exports - Heavy/Residual Fuel Oil"),
	(True,"Percent Reduction in Fossil Fuel Exports[LPG propane or butane]","Reduce Fossil Fuel Exports - LPG/Propane/Butane",[0,1],"Reduce Fossil Fuel Exports - LPG/Propane/Butane"),
	(True,"Fraction of Addressable Process Emissions Avoided via Worker Training","Worker Training",[0,1],"Worker Training"),

	# Agriculture, Land Use, and Forestry Policies
	(True,"Fraction of Afforestation and Reforestation Achieved","Afforestation and Reforestation",[0,1],"Afforestation and Reforestation"),
	(True,"Fraction of Forest Set Asides Achieved","Forest Set-Asides",[0,1],"Forest Set-Asides"),
	(True,"Fraction of Cropland Management Achieved","Cropland Management",[0,1],"Cropland Management"),
	(True,"Fraction of Improved Forest Management Achieved","Improved Forest Management",[0,1],"Improved Forest Management"),
	(True,"Fraction of Livestock Measures Achieved","Livestock Measures",[0,1],"Livestock Measures"),
	(True,"Percent Animal Products Shifted to Nonanimal Products","Shift to Non-Animal Products",[0,1],"Shift to Non-Animal Products"),

	# District Heat and Hydrogen Sector Policies
	(True,"Fraction of Non CHP Heat Production Converted to CHP","Use CHP for District Heat",[0,1],"District Heat CHP"),
	(True,"Fraction of District Heat Fuel Use Shifted to Other Fuels","Produce District Heat with Hydrogen",[0,1],"District Heat Fuel Switching"),
	(True,"Fraction of Hydrogen Production Pathways Shifted","Shift Hydrogen Production to Electrolysis",[0,1],"Hydrogen Electrolysis"),

	# Cross-Sector Policies
	(True,"Fraction of Potential Additional CCS Achieved[electricity sector]","Carbon Capture and Sequestration - Electricity Sector",[0,1],"Carbon Capture and Sequestration - Electricity Sector"),
	(True,"Fraction of Potential Additional CCS Achieved[industry sector]","Carbon Capture and Sequestration - Industry Sector",[0,1],"Carbon Capture and Sequestration - Industry Sector"),
	(True,"Additional Carbon Tax Rate[transportation sector]","Carbon Tax - Transportation Sector",[0,300],"Carbon Tax - Transportation Sector"),
	(True,"Additional Carbon Tax Rate[electricity sector]","Carbon Tax - Electricity Sector",[0,300],"Carbon Tax - Electricity Sector"),
	(True,"Additional Carbon Tax Rate[residential buildings sector]","Carbon Tax - Residential Bldg Sector",[0,300],"Carbon Tax - Residential Bldg Sector"),
	(True,"Additional Carbon Tax Rate[commercial buildings sector]","Carbon Tax - Commercial Bldg Sector",[0,300],"Carbon Tax - Commercial Bldg Sector"),
	(True,"Additional Carbon Tax Rate[industry sector]","Carbon Tax - Industry Sector",[0,300],"Carbon Tax - Industry Sector"),
	(True,"Toggle Whether Carbon Tax Affects Process Emissions","Carbon Tax Applies to Process Emissions",[0,1],"Carbon Tax on Process Emissions"),
	(True,"Percent Reduction in BAU Subsidies[hard coal]","End Existing Subsidies - Hard Coal",[0,1],"End Existing Subsidies - Hard Coal"),
	(True,"Percent Reduction in BAU Subsidies[natural gas]","End Existing Subsidies - Natural Gas",[0,1],"End Existing Subsidies - Natural Gas"),
	(True,"Percent Reduction in BAU Subsidies[nuclear]","End Existing Subsidies - Nuclear",[0,1],"End Existing Subsidies - Nuclear"),
	(True,"Percent Reduction in BAU Subsidies[solar]","End Existing Subsidies - Solar",[0,1],"End Existing Subsidies - Solar"),
	(True,"Percent Reduction in BAU Subsidies[petroleum gasoline]","End Existing Subsidies - Petroleum Gasoline",[0,1],"End Existing Subsidies - Petroleum Gasoline"),
	(True,"Percent Reduction in BAU Subsidies[petroleum diesel]","End Existing Subsidies - Petroleum Diesel",[0,1],"End Existing Subsidies - Petroleum Diesel"),
	(True,"Additional Fuel Tax Rate by Fuel[electricity]","Fuel Taxes - Electricity",[0,0.2],"Fuel Taxes - Electricity"),
	(True,"Additional Fuel Tax Rate by Fuel[hard coal]","Fuel Taxes - Hard Coal",[0,0.2],"Fuel Taxes - Hard Coal"),
	(True,"Additional Fuel Tax Rate by Fuel[natural gas]","Fuel Taxes - Natural Gas",[0,0.2],"Fuel Taxes - Natural Gas"),
	(True,"Additional Fuel Tax Rate by Fuel[petroleum gasoline]","Fuel Taxes - Petroleum Gasoline",[0,0.2],"Fuel Taxes - Petroleum Gasoline"),
	(True,"Additional Fuel Tax Rate by Fuel[petroleum diesel]","Fuel Taxes - Petroleum Diesel",[0,0.2],"Fuel Taxes - Petroleum Diesel"),

	# Research & Development Levers
	(True,"RnD Building Capital Cost Perc Reduction[heating]","Capital Cost Reduction - Buildings: Heating",[0,0.4],"Capital Cost Reduction - Buildings: Heating"),
	(True,"RnD Building Capital Cost Perc Reduction[cooling and ventilation]","Capital Cost Reduction - Buildings: Cooling and Ventilation",[0,0.4],"Capital Cost Reduction - Buildings: Cooling and Ventilation"),
	(True,"RnD Building Capital Cost Perc Reduction[envelope]","Capital Cost Reduction - Buildings: Envelope",[0,0.4],"Capital Cost Reduction - Buildings: Envelope"),
	(True,"RnD Building Capital Cost Perc Reduction[lighting]","Capital Cost Reduction - Buildings: Lighting",[0,0.4],"Capital Cost Reduction - Buildings: Lighting"),
	(True,"RnD Building Capital Cost Perc Reduction[appliances]","Capital Cost Reduction - Buildings: Appliances",[0,0.4],"Capital Cost Reduction - Buildings: Appliances"),
	(True,"RnD Building Capital Cost Perc Reduction[other component]","Capital Cost Reduction - Buildings: Other Components",[0,0.4],"Capital Cost Reduction - Buildings: Other Components"),
	(True,"RnD CCS Capital Cost Perc Reduction","Capital Cost Reduction",[0,0.4],"Capital Cost Reduction"),
	(True,"RnD Electricity Capital Cost Perc Reduction[hard coal es]","Capital Cost Reduction - Electricity: Hard Coal",[0,0.4],"Capital Cost Reduction - Electricity: Hard Coal"),
	(True,"RnD Electricity Capital Cost Perc Reduction[natural gas nonpeaker es]","Capital Cost Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"Capital Cost Reduction - Electricity: Natural Gas Nonpeaker"),
	(True,"RnD Electricity Capital Cost Perc Reduction[nuclear es]","Capital Cost Reduction - Electricity: Nuclear",[0,0.4],"Capital Cost Reduction - Electricity: Nuclear"),
	(True,"RnD Electricity Capital Cost Perc Reduction[hydro es]","Capital Cost Reduction - Electricity: Hydro",[0,0.4],"Capital Cost Reduction - Electricity: Hydro"),
	(True,"RnD Electricity Capital Cost Perc Reduction[onshore wind es]","Capital Cost Reduction - Electricity: Onshore Wind",[0,0.4],"Capital Cost Reduction - Electricity: Onshore Wind"),
	(True,"RnD Electricity Capital Cost Perc Reduction[solar PV es]","Capital Cost Reduction - Electricity: Solar PV",[0,0.4],"Capital Cost Reduction - Electricity: Solar PV"),
	(True,"RnD Electricity Capital Cost Perc Reduction[solar thermal es]","Capital Cost Reduction - Electricity: Solar Thermal",[0,0.4],"Capital Cost Reduction - Electricity: Solar Thermal"),
	(True,"RnD Electricity Capital Cost Perc Reduction[biomass es]","Capital Cost Reduction - Electricity: Biomass",[0,0.4],"Capital Cost Reduction - Electricity: Biomass"),
	(True,"RnD Electricity Capital Cost Perc Reduction[natural gas peaker es]","Capital Cost Reduction - Electricity: Natural Gas Peaker",[0,0.4],"Capital Cost Reduction - Electricity: Natural Gas Peaker"),
	(True,"RnD Electricity Capital Cost Perc Reduction[lignite es]","Capital Cost Reduction - Electricity: Lignite",[0,0.4],"Capital Cost Reduction - Electricity: Lignite"),
	(True,"RnD Electricity Capital Cost Perc Reduction[offshore wind es]","Capital Cost Reduction - Electricity: Offshore Wind",[0,0.4],"Capital Cost Reduction - Electricity: Offshore Wind"),
	(True,"RnD Industry Capital Cost Perc Reduction[cement and other carbonates]","Capital Cost Reduction - Industry: Cement",[0,0.4],"Capital Cost Reduction - Industry: Cement"),
	(True,"RnD Industry Capital Cost Perc Reduction[natural gas and petroleum systems]","Capital Cost Reduction - Industry: Natural Gas and Petroleum",[0,0.4],"Capital Cost Reduction - Industry: Natural Gas and Petroleum"),
	(True,"RnD Industry Capital Cost Perc Reduction[iron and steel]","Capital Cost Reduction - Industry: Iron and Steel",[0,0.4],"Capital Cost Reduction - Industry: Iron and Steel"),
	(True,"RnD Industry Capital Cost Perc Reduction[chemicals]","Capital Cost Reduction - Industry: Chemicals",[0,0.4],"Capital Cost Reduction - Industry: Chemicals"),
	(True,"RnD Industry Capital Cost Perc Reduction[coal mining]","Capital Cost Reduction - Industry: Mining",[0,0.4],"Capital Cost Reduction - Industry: Mining"),
	(True,"RnD Industry Capital Cost Perc Reduction[waste management]","Capital Cost Reduction - Industry: Water n Waste",[0,0.4],"Capital Cost Reduction - Industry: Water n Waste"),
	(True,"RnD Industry Capital Cost Perc Reduction[agriculture]","Capital Cost Reduction - Industry: Agriculture",[0,0.4],"Capital Cost Reduction - Industry: Agriculture"),
	(True,"RnD Industry Capital Cost Perc Reduction[other industries]","Capital Cost Reduction - Industry: Other Industries",[0,0.4],"Capital Cost Reduction - Industry: Other Industries"),
	(True,"RnD Transportation Capital Cost Perc Reduction[battery electric vehicle]","Capital Cost Reduction - Vehicles: Battery Electric",[0,0.4],"Capital Cost Reduction - Vehicles: Battery Electric"),
	(True,"RnD Transportation Capital Cost Perc Reduction[natural gas vehicle]","Capital Cost Reduction - Vehicles: Natural Gas",[0,0.4],"Capital Cost Reduction - Vehicles: Natural Gas"),
	(True,"RnD Transportation Capital Cost Perc Reduction[gasoline vehicle]","Capital Cost Reduction - Vehicles: Gasoline Engine",[0,0.4],"Capital Cost Reduction - Vehicles: Gasoline Engine"),
	(True,"RnD Transportation Capital Cost Perc Reduction[diesel vehicle]","Capital Cost Reduction - Vehicles: Diesel Engine",[0,0.4],"Capital Cost Reduction - Vehicles: Diesel Engine"),
	(True,"RnD Transportation Capital Cost Perc Reduction[plugin hybrid vehicle]","Capital Cost Reduction - Vehicles: Plug-in Hybrid",[0,0.4],"Capital Cost Reduction - Vehicles: Plug-in Hybrid"),
	(True,"RnD Transportation Capital Cost Perc Reduction[nonroad vehicle]","Capital Cost Reduction - Vehicles: Non-road",[0,0.4],"Capital Cost Reduction - Vehicles: Non-road"),
	(True,"RnD Building Fuel Use Perc Reduction[heating]","Fuel Use Reduction - Buildings: Heating",[0,0.4],"Fuel Use Reduction - Buildings: Heating"),
	(True,"RnD Building Fuel Use Perc Reduction[cooling and ventilation]","Fuel Use Reduction - Buildings: Cooling and Ventilation",[0,0.4],"Fuel Use Reduction - Buildings: Cooling and Ventilation"),
	(True,"RnD Building Fuel Use Perc Reduction[lighting]","Fuel Use Reduction - Buildings: Lighting",[0,0.4],"Fuel Use Reduction - Buildings: Lighting"),
	(True,"RnD Building Fuel Use Perc Reduction[appliances]","Fuel Use Reduction - Buildings: Appliances",[0,0.4],"Fuel Use Reduction - Buildings: Appliances"),
	(True,"RnD Building Fuel Use Perc Reduction[other component]","Fuel Use Reduction - Buildings: Other Components",[0,0.4],"Fuel Use Reduction - Buildings: Other Components"),
	(True,"RnD CCS Fuel Use Perc Reduction","Fuel Use Reduction - CCS",[0,0.4],"RnD Fuel Use Reductions - CCS"),
	(True,"RnD Electricity Fuel Use Perc Reduction[hard coal es]","Fuel Use Reduction - Electricity: Hard Coal",[0,0.4],"Fuel Use Reduction - Electricity: Hard Coal"),
	(True,"RnD Electricity Fuel Use Perc Reduction[natural gas nonpeaker es]","Fuel Use Reduction - Electricity: Natural Gas Nonpeaker",[0,0.4],"Fuel Use Reduction - Electricity: Natural Gas Nonpeaker"),
	(True,"RnD Electricity Fuel Use Perc Reduction[nuclear es]","Fuel Use Reduction - Electricity: Nuclear",[0,0.4],"Fuel Use Reduction - Electricity: Nuclear"),
	(True,"RnD Electricity Fuel Use Perc Reduction[biomass es]","Fuel Use Reduction - Electricity: Biomass",[0,0.4],"Fuel Use Reduction - Electricity: Biomass"),
	(True,"RnD Electricity Fuel Use Perc Reduction[natural gas peaker es]","Fuel Use Reduction - Electricity: Natural Gas Peaker",[0,0.4],"Fuel Use Reduction - Electricity: Natural Gas Peaker"),
	(True,"RnD Electricity Fuel Use Perc Reduction[lignite es]","Fuel Use Reduction - Electricity: Lignite",[0,0.4],"Fuel Use Reduction - Electricity: Lignite"),
	(True,"RnD Industry Fuel Use Perc Reduction[cement and other carbonates]","Fuel Use Reduction - Industry: Cement",[0,0.4],"Fuel Use Reduction - Industry: Cement"),
	(True,"RnD Industry Fuel Use Perc Reduction[natural gas and petroleum systems]","Fuel Use Reduction - Industry: Natural Gas and Petroleum",[0,0.4],"Fuel Use Reduction - Industry: Natural Gas and Petroleum"),
	(True,"RnD Industry Fuel Use Perc Reduction[iron and steel]","Fuel Use Reduction - Industry: Iron and Steel",[0,0.4],"Fuel Use Reduction - Industry: Iron and Steel"),
	(True,"RnD Industry Fuel Use Perc Reduction[chemicals]","Fuel Use Reduction - Industry: Chemicals",[0,0.4],"Fuel Use Reduction - Industry: Chemicals"),
	(True,"RnD Industry Fuel Use Perc Reduction[coal mining]","Fuel Use Reduction - Industry: Mining",[0,0.4],"Fuel Use Reduction - Industry: Mining"),
	(True,"RnD Industry Fuel Use Perc Reduction[waste management]","Fuel Use Reduction - Industry: Water n Waste",[0,0.4],"Fuel Use Reduction - Industry: Water n Waste"),
	(True,"RnD Industry Fuel Use Perc Reduction[agriculture]","Fuel Use Reduction - Industry: Agriculture",[0,0.4],"Fuel Use Reduction - Industry: Agriculture"),
	(True,"RnD Industry Fuel Use Perc Reduction[other industries]","Fuel Use Reduction - Industry: Other Industries",[0,0.4],"Fuel Use Reduction - Industry: Other Industries"),
	(True,"RnD Transportation Fuel Use Perc Reduction[battery electric vehicle]","Fuel Use Reduction - Vehicles: Battery Electric",[0,0.4],"Fuel Use Reduction - Vehicles: Battery Electric"),
	(True,"RnD Transportation Fuel Use Perc Reduction[natural gas vehicle]","Fuel Use Reduction - Vehicles: Natural Gas",[0,0.4],"Fuel Use Reduction - Vehicles: Natural Gas"),
	(True,"RnD Transportation Fuel Use Perc Reduction[gasoline vehicle]","Fuel Use Reduction - Vehicles: Gasoline Engine",[0,0.4],"Fuel Use Reduction - Vehicles: Gasoline Engine"),
	(True,"RnD Transportation Fuel Use Perc Reduction[diesel vehicle]","Fuel Use Reduction - Vehicles: Diesel Engine",[0,0.4],"Fuel Use Reduction - Vehicles: Diesel Engine"),
	(True,"RnD Transportation Fuel Use Perc Reduction[plugin hybrid vehicle]","Fuel Use Reduction - Vehicles: Plug-in Hybrid",[0,0.4],"Fuel Use Reduction - Vehicles: Plug-in Hybrid"),
	(True,"RnD Transportation Fuel Use Perc Reduction[nonroad vehicle]","Fuel Use Reduction - Vehicles: Non-road",[0,0.4],"Fuel Use Reduction - Vehicles: Non-road")
)

# Building the Policy List
# ------------------------
# Every policy, whether enabled or not, appears in a tuple called "PotentialPolicies" that was constructed above.
# Now we construct the actual list of policies to be included (named "Policies") by
# checking which of the policies have been enabled.

Policies = []
for PotentialPolicy in PotentialPolicies:
	if PotentialPolicy[Enabled]:
		Policies.append(PotentialPolicy)


# Exit with an error if no policies were enabled in the script.  We write the error to the output
# file because it's likely a user will run this without a console and won't be able to see the
# message produced by sys.exit()
if len(Policies) < 1:
	f = open(OutputScript, 'w')
	ErrorMessage = "Error: No policies were enabled in the Python script.  Before running the script, you must enable at least one policy."
	f.write(ErrorMessage)
	f.close()
	import sys
	sys.exit(ErrorMessage)


# Building the Groups List
# ------------------------
# We create a list of all the unique groups that are used by enabled policies.
Groups = []
for Policy in Policies:
	if Policy[Group] not in Groups:
		Groups.append(Policy[Group])


# Generate Vensim Command Script
# ------------------------------
# We begin by creating a new file to serve as the Vensim command script (overwriting
# any older version at that filename).  We then tell Vensim to load
# the model file, and we give it a RUNNAME that will be used for all runs.  (It is
# overwritten each run.)
f = open(OutputScript, 'w')
f.write('SPECIAL>LOADMODEL|"' + ModelFile + '"\n')
f.write("SIMULATE>RUNNAME|" + RunName + "\n")

# The following options may be useful in certain cases, but they may slow Vensim down
# or increase the odds that Vensim crashes during execution of a batch of runs (though
# it is hard to tell for sure).  These lines are usually best left commented out.
# f.write("SPECIAL>NOINTERACTION\n")
# f.write("SIMULATE>SAVELIST|" + OutputVarsFile + "\n")
f.write("\n")

def PerformRunsWithEnabledGroups():

	# First, we do a run with all of the groups disabled
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tEnabledPolicyGroup=None")
	f.write("\tEnabledPolicies=None\n\n")

	# Next, we do a run with each group enabled in turn
	for EnabledGroup in Groups:

		# We create an empty string that we'll use to track the policies enabled in each group
		EnabledPolicies=""

		# We activate policies if their group name matches the currently enabled group
		for Policy in Policies:
			if Policy[Group] == EnabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
				# We add the policy to the EnabledPolicies string
				if len(EnabledPolicies) > 0:
					EnabledPolicies += ", "
				EnabledPolicies += Policy[ShortName]

		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tEnabledPolicyGroup=" + str(EnabledGroup))
		f.write("\tEnabledPolicies=" + EnabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the policy groups enabled (a full policy case run)
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tEnabledPolicyGroup=All")
	f.write("\tEnabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdfx file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	f.write("FILE>DELETE|" + RunName + ".vdfx")
	f.write("\n\n")
	
def PerformRunsWithDisabledGroups():

	# First, we do a run with all of the groups enabled
	for Policy in Policies:
		f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
	
	# We include a SETVAL instruction to select the correct policy implementation schedule file
	f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
	
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|||||:")
	f.write("\tDisabledPolicyGroup=None")
	f.write("\tDisabledPolicies=None\n\n")

	# Next, we do a run with each group disabled in turn
	for DisabledGroup in Groups:

		# We create an empty string that we'll use to track the policies disabled in each group
		DisabledPolicies=""

		# We activate policies if their group name does not match the currently disabled group
		for Policy in Policies:
			if Policy[Group] != DisabledGroup:
				f.write("SIMULATE>SETVAL|" + Policy[LongName] + "=" + str(Policy[Settings][1]) + "\n")
			# Otherwise, we add the policy to the DisabledPolicies string
			else:
				if len(DisabledPolicies) > 0:
					DisabledPolicies += ", "
				DisabledPolicies += Policy[ShortName]
		
		# We include a SETVAL instruction to select the correct policy implementation schedule file
		f.write("SIMULATE>SETVAL|Policy Implementation Schedule Selector=" + str(PolicySchedule) + "\n")
		
		# We perform our run and log the output
		f.write("MENU>RUN|O\n")
		f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
		f.write("\tDisabledPolicyGroup=" + str(DisabledGroup))
		f.write("\tDisabledPolicies=" + DisabledPolicies + "\n\n")
	
	# Finally, we do a run with all of the groups disabled (a BAU case run)
	f.write("MENU>RUN|O\n")
	f.write("MENU>VDF2TAB|" + RunName + ".vdfx|" + RunResultsFile + "|" + OutputVarsFile + "|+!||||:")
	f.write("\tDisabledPolicyGroup=All")
	f.write("\tDisabledPolicies=All")
	f.write("\n")

	# We instruct Vensim to delete the .vdfx file, to prevent it from getting picked up by
	# sync software, such as DropBox or Google Drive.  If sync software locks the file,
	# Vensim won't be able to overwrite it on the next model run, ruining the batch.
	# Due to file format changes in Vensim 8, the command needs a different file extenstion
	# depending on whether this script is run in Vensim 7 or Vensim 8.
	# Vensim 7:
	# f.write("FILE>DELETE|" + RunName + ".vdfx")
	# Vensim 8:
	f.write("FILE>DELETE|" + RunName + ".vdfxx")
	f.write("\n\n")
	
if EnableOrDisableGroups == "Enable":
	PerformRunsWithEnabledGroups()
else:
	PerformRunsWithDisabledGroups()

# We are done writing the Vensim command script and therefore close the file.
f.close()