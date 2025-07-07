from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsername
username = getUsername()

###############################################################################
# INPUT/OUTPUT SETTINGS

jobTag = 'Run3_OXY_pO_Pythia_Angantyr_9617GeV'
#jobTag = 'Run3_OXY_pO_PYTHIA_Angantyr'
#jobTag = 'Run3_OXY_pO_EPOS_LHC'
input = '/MinBias_Pythia_Angantyr_pO_9617GeV/wangj-MINIAOD_250626_el8_Run3_2025_OXY_1509p1-60a2506526396861a6a1b0c3fe3e8168/USER'
inputDatabase = 'phys03'
output = '/store/group/phys_heavyions/' + username + '/Run3_OXY_2025MC_QuickForest/'
outputServer = 'T2_CH_CERN'

###############################################################################

config = config()

config.General.requestName = jobTag
config.General.workArea = 'CrabWorkArea'
config.General.transferOutputs = True

config.JobType.psetName = 'forest_CMSSWConfig_Run3_OXY_MC_miniAOD.py'
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 5000
config.JobType.pyCfgParams = ['noprint']
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = input
config.Data.inputDBS = inputDatabase
config.Data.unitsPerJob = 10000
config.Data.totalUnits = -1
config.Data.splitting = 'EventAwareLumiBased'
config.Data.publication = False
config.Data.outLFNDirBase = output
config.Site.storageSite = outputServer
