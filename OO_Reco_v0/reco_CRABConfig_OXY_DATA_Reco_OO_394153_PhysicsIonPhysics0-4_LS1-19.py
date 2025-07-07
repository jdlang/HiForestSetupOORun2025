from CRABClient.UserUtilities import config
config = config()
config.General.transferOutputs = True
# ==============================
config.General.requestName = 'MINIAOD_OO_394153_PhysicsIonPhysics0-4_LS1-19'
inputList = 'filelist_OO_394153_PhysicsIonPhysics0-4_LS1-19.txt'
config.Data.userInputFiles = open(inputList).readlines()
# ==============================
config.General.workArea = 'CrabWorkArea'
config.JobType.psetName = 'reco2miniaod_RAW2DIGI_L1Reco_RECO_PAT.py'
config.JobType.numCores = 8

config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 5000
config.JobType.pyCfgParams = ['noprint']
config.JobType.allowUndistributedCMSSW = True

##
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.splitting = 'FileBased'
config.Data.publication = False

##
config.Site.storageSite = 'T2_CH_CERN'
config.Data.outLFNDirBase = '/store/group/phys_heavyions/jdlang/Run3_OO_QuickReco/Run3_OO_2025Data_QuickForest'
config.Site.whitelist = ['T2_CH_CERN']


