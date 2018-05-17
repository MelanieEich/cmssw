import FWCore.ParameterSet.Config as cms
import os
import copy

import SimTracker.TrackAssociatorProducers.trackAssociatorByHits_cfi as tabh

processName = "TruthMatching"
process = cms.Process(processName)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False),
    allowUnscheduled = cms.untracked.bool(True),
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("SimTracker.TrackHistory.VertexClassifier_cff")
process.vertexClassifier.vertexProducer = cms.untracked.InputTag("inclusiveSecondaryVertices")
#process.vertexClassifier.vertexProducer = cms.untracked.InputTag("offlinePrimaryVertices")
process.vertexHistory.vertexProducer = cms.untracked.InputTag("inclusiveSecondaryVertices") 
#process.vertexHistory.vertexProducer = cms.untracked.InputTag("offlinePrimaryVertices") 
#process.vertexHistory.enableSimToReco = cms.untracked.bool(True) 

process.ak4JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    tracks = cms.InputTag("generalTracks"),
    coneSize = cms.double(0.4),
    useAssigned = cms.bool(True),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    jets = cms.InputTag("ak4PFJetsCHS")
)


process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_mc")

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)

process.load("RecoBTag.ImpactParameter.impactParameterTagInfos_cfi")
process.impactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")

# SecondaryVertexProducer using IVF Vertex collection
process.load("RecoBTag.SecondaryVertex.secondaryVertexTagInfos_cfi")
process.secondaryVertexTagInfos.extSVCollection = cms.InputTag("inclusiveSecondaryVertices")
process.secondaryVertexTagInfos.vertexCuts.distVal2dMax = cms.double(99999.9)
process.secondaryVertexTagInfos.vertexCuts.distSig2dMin = cms.double(-99999.9)
process.vertexCutsBlock.vertexCuts.distVal2dMax = cms.double(99999.9)
process.vertexCutsBlock.vertexCuts.distSig2dMin = cms.double(-99999.9)
process.secondaryVertexTagInfos.useExternalSV = cms.bool(True)
process.secondaryVertexTagInfos.useSVClustering = cms.bool(True)
process.secondaryVertexTagInfos.jetAlgorithm = cms.string("AntiKt")
process.secondaryVertexTagInfos.rParam = cms.double(0.4)

#process.load("RecoBTag.SecondaryVertex.secondaryVertexTagInfosDefault_cfi")

# SecondaryVertexProducer using CSV VertexCompositePtrCandidate
# process.load("RecoBTag.SecondaryVertex.pfSecondaryVertexTagInfos_cfi")
# process.pfSecondaryVertexTagInfos.extSVCollection = cms.InputTag("inclusiveCandidateSecondaryVertices")
# process.pfSecondaryVertexTagInfos.useExternalSV = cms.bool(True)
# process.vertexCutsBlock.vertexCuts.distVal2dMax = cms.double(99999.9)
# process.vertexCutsBlock.vertexCuts.distSig2dMin = cms.double(-99999.9)
# process.pfSecondaryVertexTagInfos.useSVClustering = cms.bool(True)
# process.pfSecondaryVertexTagInfos.jetAlgorithm = cms.string("AntiKt")
# process.pfSecondaryVertexTagInfos.rParam = cms.double(0.4)


process.load("SimTracker.TrackHistory.SecondaryVertexTagInfoProxy_cff")
process.svTagInfoProxy.svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos")

process.load("PhysicsTools.UtilAlgos.TFileService_cfi")

process.svTagInfoValidation = cms.EDAnalyzer("SVTagInfoValidationAnalyzer",
#    svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos"),
    svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos"),
    bestMatchByMaxValue = cms.untracked.bool(True),
    trackingTruth = cms.untracked.InputTag('mix','MergedTrackTruth'),
    vertexAssociator = cms.untracked.InputTag('vertexAssociatorByTracksByHits'),
#    vertexProducer = cms.untracked.InputTag('offlinePrimaryVertices'),
    vertexProducer = cms.untracked.InputTag('svTagInfoProxy'),
    enableRecoToSim = cms.untracked.bool(True),
    enableSimToReco = cms.untracked.bool(False),
    hepMC = cms.untracked.InputTag("generatorSmeared"),
    longLivedDecayLength = cms.untracked.double(1e-14),
    vertexClusteringDistance = cms.untracked.double(0.003)
)

# process.svTagInfoProxyValidation = cms.EDAnalyzer("SVTagInfoProxyAnalyzer",
#     svTagInfoProducer = cms.untracked.InputTag("secondaryVertexTagInfos"),
#     vertexProxyColl = cms.untracked.InputTag("svTagInfoProxy"),
#     bestMatchByMaxValue = cms.untracked.bool(True),
#     trackingTruth = cms.untracked.InputTag('mix','MergedTrackTruth'),
#     vertexAssociator = cms.untracked.InputTag('vertexAssociatorByTracksByHits'),
#     vertexProducer = cms.untracked.InputTag('offlinePrimaryVertices'),
#     enableRecoToSim = cms.untracked.bool(True),
#     enableSimToReco = cms.untracked.bool(False),
#     hepMC = cms.untracked.InputTag("generatorSmeared"),
#     longLivedDecayLength = cms.untracked.double(1e-14),
#     vertexClusteringDistance = cms.untracked.double(0.003)
# )

process.trackingParticleRecoTrackAsssociationByHits.associator = cms.InputTag("quickTrackAssociatorByHits")


process.vertexHistoryAnalyzer = cms.EDAnalyzer("VertexHistoryAnalyzer",
    process.vertexClassifier
)


# process.source = cms.Source ("PoolSource",
#     fileNames=cms.untracked.vstring(
# #        'file:////nfs/dust/cms/user/eichm/btag/data/bgd/84B70053-DA98-E711-8525-00259029E87C.root'
# #        'file:////nfs/dust/cms/user/eichm/btag/data/2016/00104622-EA3C-E611-807A-002590200828.root'
# #        'file:////nfs/dust/cms/user/eichm/btag/ntuple/NI_QCD17.root'
# #        'file:////nfs/dust/cms/user/eichm/btag/data/2017/RunIIFall17DRPremix_QCD_Pt_50to80_TuneCP5_13TeV_pythia8/4299C2F1-4FDC-E711-938D-A4BF0112BC52.root'
# #        'file:////nfs/dust/cms/user/eichm/btag/data/2017/RunIIFall17DRPremix_QCD_Pt_80to120_TuneCP5_13TeV_pythia8/72CD356F-4BDC-E711-885D-0242AC130002.root'
#         'file:////store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/008D9025-4CDC-E711-A398-0242AC130002.root'
#     )
# )

# source for QCD Pt 80 to 120 GeV
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
        '/store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/008D9025-4CDC-E711-A398-0242AC130002.root'
#        '/store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/72CD356F-4BDC-E711-885D-0242AC130002.root'
#        '/store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/7A8DF3B6-E2DB-E711-BEEB-0242AC130002.root'
#        '/store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/BC680365-52DC-E711-B825-FA163E04137F.root'
#        '/store/mc/RunIIFall17DRPremix/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/CA84E2A4-4FDC-E711-A204-FA163EC5DEF2.root' 
  )
)

# # source for QCD Pt 50 to 80 GeV
# process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
# #        'file:////nfs/dust/cms/user/eichm/btag/data/2017/RunIIFall17DRPremix_QCD_Pt_50to80_TuneCP5_13TeV_pythia8/4299C2F1-4FDC-E711-938D-A4BF0112BC52.root'
# #        '/store/mc/RunIIFall17DRPremix/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/6C16CBF4-CEDC-E711-BCEC-001E67792624.root'
# #         '/store/mc/RunIIFall17DRPremix/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/6E333461-53DC-E711-BFD8-3417EBE520BA.root'
# #         '/store/mc/RunIIFall17DRPremix/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/40000/E407AD92-4FDC-E711-AEFE-0025901D48AA.root'
#   )
# )

# # source for QCD Pt 170 to 300 GeV
# process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring(
# #'/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/1841250C-E3DA-E711-A688-FA163EF578FC.root'
# '/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/5E6592B7-15DA-E711-8437-FA163EB1639C.root'
# #'/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/86BC0AA6-56DB-E711-9D9E-FA163E2A55D6.root'
# #'/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/9A47C2E1-0EDC-E711-8663-008CFAC93FDC.root'
# #'/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/D4E9D3D8-06DC-E711-81C8-008CFAE451F8.root'
# #'/store/mc/RunIIFall17DRPremix/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/GEN-SIM-RECODEBUG/94X_mc2017_realistic_v10-v1/60000/F26791B2-56DB-E711-BE07-02163E012D5B.root'
#   )
# )


process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string("/nfs/dust/cms/user/eichm/btag/ntuple/vertex_QCD_170to300_3.root"),
#    fileName = cms.untracked.string("/store/user/meich/NI_identification/vertex_QCD_default_test.root"),
    fileName = cms.untracked.string("vertex_QCD_default_test_few.root"),
    outputCommands = cms.untracked.vstring("drop *",
                        "keep *_*_*_TruthMatching",
                        "keep *_inclusiveSecondaryVertices_*_*",
                        "keep *_offlinePrimaryVertices_*_*",
                        "keep *_mix_MergedTrackTruth_*")
)

process.vertexAssociatorSequence = cms.Sequence( process.tpClusterProducer * process.quickTrackAssociatorByHits* process.trackingParticleRecoTrackAsssociationByHits * process.ak4JetTracksAssociatorAtVertexPF * process.vertexAssociatorByTracksByHits * process.impactParameterTagInfos * process.secondaryVertexTagInfos )

process.p = cms.Path( process.vertexAssociatorSequence  * process.svTagInfoProxy *  process.svTagInfoValidation)

#  * process.svTagInfoProxyValidation * process.vertexHistoryAnalyzer *

process.e = cms.EndPath(process.out)

outFile = open("tmpConfig_vertex.py","w")
outFile.write(process.dumpPython())
outFile.close()
