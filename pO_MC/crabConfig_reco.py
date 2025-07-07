#

from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True 
config.General.requestName = 'RECO_250626_Pythia_Angantyr_OO_5362GeV'
config.Data.inputDataset = '/MinBias_Pythia_Angantyr_OO_5362GeV/wangj-DIGIRAW_250626_el8_gcc12_1508-477c5f536820d41c056e64b7f7215084/USER'
config.General.workArea = 'crab_projects'
config.JobType.psetName = 'reco_RAW2DIGI_L1Reco_RECO_RECOSIM.py'
config.JobType.pluginName = 'Analysis' 
config.JobType.maxMemoryMB = 5000 
config.JobType.pyCfgParams = ['noprint']
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True

##
config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 1 ## 
config.Data.totalUnits = -1 
config.Data.splitting = 'FileBased'
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = True
config.Data.outputDatasetTag = 'AOD_250626_el8_Run3_2025_OXY_1508'

##
config.Site.storageSite = 'T2_US_Vanderbilt'
# config.Site.blacklist = ['T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T3_US_Rutgers','T3_BG_UNI_SOFIA','T3_IT_Perugia']
# config.Site.whitelist = ['T2_US_MIT'] 
config.Site.ignoreGlobalBlacklist = True
config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
