#

from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True 
config.General.requestName = 'MINIAOD_250626_Pythia_Angantyr_OO_5362GeV'
config.Data.inputDataset = '/MinBias_Pythia_Angantyr_OO_5362GeV/loizides-AOD_250626_el8_Run3_2025_OXY_1508-14f424f0adbe361d4995c06343c1ab4f/USER'
config.General.workArea = 'crab_projects'
config.JobType.psetName = 'miniaod_PAT.py'
config.JobType.pluginName = 'Analysis' 
config.JobType.maxMemoryMB = 2500 
config.JobType.pyCfgParams = ['noprint']
# config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

##
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 2 ## 
config.Data.totalUnits = -1 
config.Data.splitting = 'FileBased'
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = True
config.Data.outputDatasetTag = 'MINIAOD_250626_el8_Run3_2025_OXY_1508'

##
config.Site.storageSite = 'T2_US_Vanderbilt'
# config.Site.blacklist = ['T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T3_US_Rutgers','T3_BG_UNI_SOFIA','T3_IT_Perugia']
# config.Site.whitelist = ['T2_US_MIT'] 
config.Site.ignoreGlobalBlacklist = True
config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
