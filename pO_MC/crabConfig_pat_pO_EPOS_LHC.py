#

from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True 
config.General.requestName = 'MINIAOD_250703_Epos_LHC_pO_9617GeV'
config.Data.inputDataset = '/MinBias_EposLHC_ReggeGribovParton_pO_9617GeV/jdlang-AOD_Run3OXY_EposLHC_pO_9617GeV_250704_el8_1509p1-08768d006a17fc4cf96696220a495928/USER'
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
config.Data.outputDatasetTag = 'MINIAOD_Run3OXY_EposLHC_pO_9617GeV_250704_el8_1509p1'

##
config.Site.storageSite = 'T2_US_Vanderbilt'
# config.Site.blacklist = ['T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T3_US_Rutgers','T3_BG_UNI_SOFIA','T3_IT_Perugia']
# config.Site.whitelist = ['T2_US_MIT'] 
config.Site.ignoreGlobalBlacklist = True
config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
